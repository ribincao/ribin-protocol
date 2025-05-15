import fsbot
import json
import os

pr_title = os.environ.get("pr_title", "")
pr_url = os.environ.get("pr_url", "")
pr_user = os.environ.get("pr_user", "")
pr_type = os.environ.get("pr_type", "")
reviewers = os.environ.get("reviewers", [])  # type: ignore
review_user = os.environ.get("review_user", "")
merge_user = os.environ.get("merge_user", "")

backend_email_dic = {
    "MarcoQin": "qinyuanyuan@kuse.ai",
    "sfzman": "fangzhou@kuse.ai",
    "ribincao": "ribin@kuse.ai",
    "austinxu123": "x@kuse.ai",
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
        if pr_type == "reviewed":
            self.event_name = "KUSE-Backend (global) Request Approved ✅ "
            self.content = self.pr_reviewed_content(pr_title, pr_user, pr_url)
        elif pr_type == "created":
            self.event_name = "KUSE-Backend (global) Pull Request 🚀 "
            self.content = self.pr_create_content(pr_title, pr_user, pr_url)
        elif pr_type == "merged":
            self.event_name = "KUSE-Backend (global) Pull Request Merged 👏 "
            self.content = self.pr_merged_content(pr_title, pr_user, pr_url)

    def send_message(self):
        """
        发送消息
        """
        if pr_type == "created":
            self.content.append(self.get_at_list(reviewers))
        feishu = fsbot.FeishuMessageBot(self.webhook, secret=self.secret)
        rich_text = self.create_rich_text(self.event_name, self.content)
        feishu.post(rich_text)

    def get_at_list(self, reviewers: str):
        """
        生成@用户富文本
        :param reviewers: pull request中要求reivew的人
        """
        text = "reviewers: "
        reviewers_list = json.loads(reviewers)
        for reviewer in reviewers_list:
            email = backend_email_dic.get(reviewer, "")
            if not email:
                continue
            text += f"<at email={email}>"
        at_lsit = [
            {"tag": "text", "text": text},
        ]
        return at_lsit

    def pr_create_content(self, desc: str, user: str, url: str):
        """
        初始化PR创建富文本内容
        :param desc: PR描述
        :param user: 发起user的人
        """
        content = [
            [
                {"tag": "text", "text": "Desc：" + desc},
            ],
            [],
            [
                {"tag": "text", "text": f"Request：{backend_email_dic.get(user, '')}"},
            ],
            [],
            [
                {"tag": "text", "text": f"PR Link：{url}"},
            ],
            [],
        ]
        return content

    def pr_reviewed_content(self, desc: str, user: str, url: str):
        """
        初始化PR完成代码审查富文本内容
        :param desc: PR描述
        :param user: 发起user的人
        """
        content = [
            [
                {"tag": "text", "text": "Desc：" + desc},
            ],
            [],
            [
                {"tag": "text", "text": f"Request：{backend_email_dic.get(user, '')}"},
            ],
            [],
            [
                {"tag": "text", "text": f"PR Link：{url}"},
            ],
            [],
            [
                {
                    "tag": "text",
                    "text": f"reviewer：<at email={backend_email_dic.get(review_user, '')}>",
                },
            ],
        ]
        return content

    def create_rich_text(self, title: str, content: str):
        """
        创建富文本
        :param title: 标题
        :param content: 富文本内容
        """
        rich_text = {
            "msg_type": "post",
            "content": {"post": {"zh_cn": {"title": title, "content": content}}},
        }
        return rich_text

    def pr_merged_content(self, desc: str, user: str, url: str):
        """
        初始化PR完成代码审查富文本内容
        :param desc: PR描述
        :param user: 发起user的人
        """

        email = backend_email_dic.get(user, "")
        content = [
            [
                {"tag": "text", "text": "Desc：" + desc},
            ],
            [],
            [
                {"tag": "text", "text": f"Request： <at email={email}>"},
            ],
            [],
            [
                {"tag": "text", "text": f"PR Link：{url}"},
            ],
            [],
            [
                {
                    "tag": "text",
                    "text": f"merge：<at email={backend_email_dic.get(merge_user, '')}>",
                },
            ],
        ]
        return content


if __name__ == "__main__":
    noti = PrNotification()
    noti.send_message()
