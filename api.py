# -*- coding: utf-8 -*-
import web
import tags, getCaipu, getIDFromTag, getIDFromName, urls, urlHandler

urls = (
    '/', 'api'
)
app = web.application(urls, globals())
class api:
    def GET(self):
        content = web.input()['caipu']
        print content
        if content in tags.tags.keys():
            #response = wechat.response_text(tags.tags[content])
            id_list = getIDFromTag.getIDFromTag(tags.tags[content])
        else:
            id_list = getIDFromName.getIDFromName(content)
        if id_list:
            news_list = []
            for id in id_list:
                caipu = getCaipu.getCaipu(id)
                news_map = {
                    'title': caipu['title'],
                    'description': caipu['description'],
                    'picurl': caipu['picurl'],
                    #'url':'http://104.131.156.81/test'
                    'url': caipu['url']
                }
                news_list.append(news_map)
            return news_list
        else:
            return u'不能识别'

if __name__ == '__main__':
    app.run()