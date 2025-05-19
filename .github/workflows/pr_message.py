import fsbot
import json
import os

pr_title = os.environ.get("pr_title", "")
pr_url = os.environ.get("pr_url", "")
pr_user = os.environ.get("pr_user", "")
pr_type = os.environ.get("pr_type", "")
reviewers = os.environ.get("reviewers", "[]")  # type: ignore
review_user = os.environ.get("review_user", "")
merge_user = os.environ.get("merge_user", "")


def get_title() -> str:
    pr_title = os.environ.get("pr_title", "")
    if pr_title:
        return pr_title

    with open("commit_diff.txt", "r") as f:
        commit_log = f.read()
    return commit_log


backend_email_dic = {
    "ribincao": "ribin@kuse.ai",
}
pr_color_dict = {
    "created": "yellow",
    "reviewed": "blue",
    "merged": "green",
    "push": "red",
    "release": "green",
}
pr_event_dict = {
    "created": "KUSE-Backend (kuse_ai) Pull Request 👀 ",
    "reviewed": "KUSE-Backend (kuse_ai) Request Approved ✅ ",
    "merged": "KUSE-Backend (kuse_ai) Pull Request Merged 👏 ",
    "push": "KUSE-Backend (kuse_ai) Main Pushed 🚀 ",
    "release": "KUSE-Backend (kuse_ai) Release ",
}


class PrNotification:
    def __init__(self):
        """
        机器人初始化
        :param webhook: 飞书群自定义机器人webhook地址
        :param secret: 机器人安全设置页面勾选“加签”时需要传入的密钥
        :param content: 富文本初始化内容
        """

        self.webhook = "https://open.larksuite.com/open-apis/bot/v2/hook/32bcd6a0-db67-456f-8f9c-525e4c3cc3aa"
        self.secret = ""
        self.pr_type = pr_type

        self.color = pr_color_dict.get(self.pr_type, "red")
        self.event_name = pr_event_dict.get(self.pr_type, "")
        self.at_users = (
            self.get_all_list()
            if self.pr_type == "push"
            else self.get_at_list(reviewers)
        )
        self.pr_user = backend_email_dic.get(pr_user, "")
        self.pr_title = get_title()
        self.pr_url = pr_url
        self.merge_user = merge_user

    def send_message(self):
        """
        发送消息
        """
        feishu = fsbot.FeiShuMessageBot(self.webhook, secret=self.secret)
        feishu.post(self.create_rich_text())

    def get_all_list(self) -> str:
        """
        获取所有通知用户
        """
        text = ""
        for _, email in backend_email_dic.items():
            text += f"<at email={email}></at>"
        return text

    def get_at_list(self, reviewers: str) -> str:
        """
        生成@用户富文本
        :param reviewers: pull request中要求reivew的人
        """
        reviewers_list = json.loads(reviewers)
        if not reviewers_list:
            return ""
        text = ""
        for reviewer in reviewers_list:
            email = backend_email_dic.get(reviewer, "")
            if not email:
                continue
            text += f"<at email={email}></at>"
        return text

    def create_rich_text(self):
        """
        创建富文本卡片
        :param title: 标题
        :param content: 富文本内容
        """
        rich_text = {
            "msg_type": "interactive",
            "card": {
                "config": {
                    "wide_screen_mode": True,
                },
                "header": {
                    "template": self.color,
                    "title": {"content": self.event_name, "tag": "plain_text"},
                },
                "elements": [
                    {
                        "fields": [
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**👤 User：**<at email={self.pr_user}></at>",
                                    "tag": "lark_md",
                                },
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**🔢 Desc：**{self.pr_title}",
                                    "tag": "lark_md",
                                },
                            },
                            {
                                "is_short": True,
                                "text": {
                                    "content": f"**🔎 Link：**{self.pr_url} </at>",
                                    "tag": "lark_md",
                                },
                            },
                        ],
                        "tag": "div",
                    }
                ],
            },
        }
        if self.at_users:
            rich_text["card"]["elements"][0]["fields"].append(
                {
                    "is_short": True,
                    "text": {
                        "content": f"**💪 Reviewers：**{self.at_users}",
                        "tag": "lark_md",
                    },
                }
            )
        if self.pr_type == "merged":
            rich_text["card"]["elements"][0]["fields"].append(
                {
                    "is_short": True,
                    "text": {
                        "content": f"**👏 Merged：**<at email={backend_email_dic.get(self.merge_user, '')}></at>",
                        "tag": "lark_md",
                    },
                }
            )

        return rich_text


if __name__ == "__main__":
    noti = PrNotification()
    noti.send_message()
