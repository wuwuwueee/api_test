import requests

class Topics(object):
    base_url = 'http://39.107.96.138:3000/api/v1'

    #class构造器
    def __init__(self,url):
        #拼接完整的接口URL
        self.url = self.base_url + url

    #1
    # get /topics 主题首页
    def get_data_topics(self,limit,tab):
        #get方式参数params
        params = {
            'limit':limit,
            'tab':tab
        }
        r = requests.get(self.url,params = params)
        return r

    #2
    # post /topics 新建主题
    def post_create_topics(self,title,tab,content,accesstoken):
        data = {
            'accesstoken':accesstoken,
            'title':title,
            'tab':tab,
            'content':content
        }
        r = requests.post(self.url,data = data)
        return r

    #3
    # get /topic/:id 主题详情
    def get_details_topics(self,accesstoken):
        params = {
            'accesstoken':accesstoken
        }
        r = requests.get(self.url,params = params)
        return r

    #4
    # post /topics/update 编辑主题
    def post_update_topics(self,accesstoken,title,tab,content,topic_id):
        data = {
            'accesstoken':accesstoken,
            'title':title,
            'tab':tab,
            'content':content,
            'topic_id':topic_id
        }
        r = requests.post(self.url,data = data)
        return r

    #5
    # post /topic_collect/collect 收藏主题
    def post_collection_topics(self,accesstoken,topic_id):
        data = {
            'accesstoken':accesstoken,
            'topic_id ':topic_id 
            }
        r = requests.post(self.url,data = data)
        return r
    
    #6
    # post /topic_collect/de_collect 取消主题
    def post_cancel_topics(self,accesstoken,topic_id):
        data = {
            'accesstoken':accesstoken,
            'topic_id ':topic_id 
            }
        r = requests.post(self.url,data = data)
        return r

    #7
    # get /topic_collect/:loginname 用户所收藏的主题
    def get_collect_topics(self):
        r = requests.get(self.url)
        return r

  
    
    #8
    # post /topic/:topic_id/replies 新建评论
    def post_first_comment_topics(self,accesstoken,content):
        data = {
            'accesstoken':accesstoken,
            'content':content
        }
        r = requests.post(self.url,data = data)
        return r

    def post_second_comment_topics(self,accesstoken,content,reply_id):
        data = {
            'accesstoken':accesstoken,
            'content':content,
            'reply_id':reply_id
        }
        r = requests.post(self.url,data = data)
        return r

    #9
    # post /reply/:reply_id/ups 为评论点赞
    def post_fabulous_topics(self,accesstoken):
        data = {
            'accesstoken':accesstoken
        }
        r = requests.post(self.url,data = data)
        return r
 
    10
    # get /user/:loginname 用户详情
    def get_user_topics(self):
        r = requests.get(self.url)
        return r
    
    #11
    # post /accesstoken 验证 accessToken 的正确性
    def post_verify_topics(self,accesstoken ):
        data = {
            'accesstoken':accesstoken 
        }
        r = requests.post(self.url,data = data)
        return r


    #12
    #get /message/count 获取未读消息数
    def get_message_n_topics(self,accesstoken):
        params = {
            'accesstoken':accesstoken
        }
        r = requests.get(self.url,params = params)
        return r



    #13
    #get /messages 获取已读和未读消息
    def get_message_all_topics(self,accesstoken):
        params = {
            'accesstoken':accesstoken
        }
        r = requests.get(self.url,params = params)
        return r

    #14
    #post /message/mark_all 标记全部已读
    def post_message_mark_all_topics(self,accesstoken):
        data = {
            'accesstoken':accesstoken 
        }
        r = requests.post(self.url,data = data)
        return r

    #15
    #post /message/mark_one/:msg_id 标记单个消息为已读
    def post_message_mark_one_topics(self,accesstoken):
        data = {
            'accesstoken':accesstoken 
        }
        r = requests.post(self.url,data = data)
        return r
    
    



