# -*- coding: utf-8 -*-
import json
import os
import sys
current_path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(current_path)
import unittest
from common.myGlobal import SMS_message
from common.myLogger import logger
from common.myRequest import request_post
from common.readConfig import read_config

cfg = read_config(os.path.dirname(os.path.dirname(__file__)) + '/cfg/config.ini')
base_url = cfg.get('base_para', 'base_url')
robot_url = cfg.get('base_para', 'robot_url')


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base_url = base_url
        cls.path_code = {
                "T01": [r"/recommendArticle", "文章推荐结果查询接口"],
                "T02": [r"/recommendProject", "项目推荐结果查询接口"],
                "T03": [r"/recommendBusiness", "商机推荐结果查询接口"],
                "T04": [r"/recommendPjctPlayback", "项目回放推荐结果查询接口"],
                "T05": [r"/relationArticle", "文章相关文章查询接口"],
                "T06": [r"/relationProject", "项目相关项目查询接口"],
                "T07": [r"/relationArticleProject", "文章相关项目查询接口"],
                "T08": [r"/recommendPjctTab", "项目二级栏目推荐结果查询接口"],
                "T09": [r"/recommendPjctTabContent", "项目二级栏目推荐内容结果查询接口"],
                "T10": [r"/recommendVideo", "视频推荐结果查询接口"]
            }
        cls.user_id = "2152652"

    @classmethod
    def tearDownClass(cls):
        pass

    def test001(self):
        """文章推荐结果查询接口/文章相关文章查询接口/文章相关项目查询接口"""
        url_T01 = f'{self.base_url}{self.path_code["T01"][0]}'
        data_T01 = {
            "userId": self.user_id,
            "rcmdNum": 10,
            "pageNum": 1
        }
        res_text_T01 = request_post(url_T01, data_T01)
        try:
            res_dict_T01 = json.loads(res_text_T01)
            if res_dict_T01["code"] != 1000:
                case_message_T01 = {
                            "case_num": "T01",
                            "description": f'{self.path_code["T01"][1]}——————接口响应异常',
                            "log": f"{res_text_T01}"
                        }
                SMS_message.append(case_message_T01)
            else:
                if len(res_dict_T01["recommendation"]) == 0:
                    case_message_T01 = {
                        "case_num": "T01",
                        "description": f'{self.path_code["T01"][1]}——推荐列表返回为空',
                        "log": f"{res_text_T01}"
                    }
                    SMS_message.append(case_message_T01)
                else:   # 执行T05/T07接口
                    # 执行T05接口
                    url_T05 = f'{self.base_url}{self.path_code["T05"][0]}'
                    data_T05 = {
                        "articleId": res_dict_T01["recommendation"][0]["id"],
                        "rcmdNum": 3,
                        "pageNum": 1
                    }
                    res_text_T05= request_post(url_T05, data_T05)
                    res_dict_T05 = json.loads(res_text_T05)
                    if res_dict_T05["code"] != 1000:
                        case_message_T05 = {
                            "case_num": "T05",
                            "description": f'{self.path_code["T05"][1]}——接口响应异常',
                            "log": f"{res_text_T05}"
                        }
                        SMS_message.append(case_message_T05)
                    else:
                        if len(res_dict_T05["recommendation"]) != 3:
                            case_message_T05 = {
                                "case_num": "T05",
                                "description": f'{self.path_code["T05"][1]}——推荐列表返回为空或不足3条',
                                "log": f"{res_text_T05}"
                            }
                            SMS_message.append(case_message_T05)
                        else:
                            pass
                    # 执行T07接口
                    url_T07 = f'{self.base_url}{self.path_code["T07"][0]}'
                    data_T07 = {
                        "articleId": res_dict_T01["recommendation"][0]["id"],
                        "rcmdNum": 3,
                        "pageNum": 1
                    }
                    res_text_T07 = request_post(url_T07, data_T07)
                    res_dict_T07 = json.loads(res_text_T07)
                    if res_dict_T07["code"] != 1000:
                        case_message_T07 = {
                            "case_num": "T07",
                            "description": f'{self.path_code["T07"][1]}——接口响应异常',
                            "log": f"{res_text_T07}"
                        }
                        SMS_message.append(case_message_T07)
                    else:
                        if len(res_dict_T07["recommendation"]) != 3:
                            case_message_T07 = {
                                "case_num": "T07",
                                "description": f'{self.path_code["T07"][1]}——推荐列表返回为空或不足3条',
                                "log": f"{res_text_T07}"
                            }
                            SMS_message.append(case_message_T07)
                        else:
                            pass
        except Exception as msg:
            case_message = {
                "case_num": "T01/T05/T07",
                "description": 'T01/T05/T07接口——服务响应异常'
            }
            SMS_message.append(case_message)
            logger.error(f"系统异常记录:{case_message}；报错信息：{msg}")

    def test002(self):
        """项目推荐结果查询接口/项目相关项目查询接口"""
        url_T02 = f'{self.base_url}{self.path_code["T02"][0]}'
        data_T02 = {
            "userId": self.user_id,
            "rcmdNum": 10,
            "pageNum": 1
        }
        res_text_T02 = request_post(url_T02, data_T02)
        try:
            res_dict_T02 = json.loads(res_text_T02)
            if res_dict_T02["code"] != 1000:
                case_message_T02 = {
                            "case_num": "T02",
                            "description": f'{self.path_code["T02"][1]}——接口响应异常',
                            "log": f"{res_text_T02}"
                        }
                SMS_message.append(case_message_T02)
            else:
                if len(res_dict_T02["recommendation"]) == 0:
                    case_message_T02 = {
                        "case_num": "T02",
                        "description": f'{self.path_code["T02"][1]}——推荐列表返回为空',
                        "log": f"{res_text_T02}"
                    }
                    SMS_message.append(case_message_T02)
                else:
                    # 执行T06接口
                    url_T06 = f'{self.base_url}{self.path_code["T06"][0]}'
                    data_T06 = {
                        "projectId": res_dict_T02["recommendation"][0]["id"],
                        "rcmdNum": 3,
                        "pageNum": 1
                    }
                    res_text_T06 = request_post(url_T06, data_T06)
                    res_dict_T06 = json.loads(res_text_T06)
                    if res_dict_T06["code"] != 1000:
                        case_message_T06 = {
                            "case_num": "T06",
                            "description": f'{self.path_code["T06"][1]}——接口响应异常',
                            "log": f"{res_text_T06}"
                        }
                        SMS_message.append(case_message_T06)
                    else:
                        if len(res_dict_T06["recommendation"]) != 3:
                            case_message_T06 = {
                                "case_num": "T06",
                                "description": f'{self.path_code["T06"][1]}——推荐列表返回为空或不足3条',
                                "log": f"{res_text_T06}"
                            }
                            SMS_message.append(case_message_T06)
                        else:
                            pass
        except Exception as msg:
            case_message = {
                "case_num": "T02/T06",
                "description": 'T02/T06接口——服务响应异常'
            }
            SMS_message.append(case_message)
            logger.error(f"系统异常记录:{case_message}；报错信息：{msg}")

    def test003(self):
        """商机推荐结果查询接口"""
        url_T03 = f'{self.base_url}{self.path_code["T03"][0]}'
        data_T03 = {
            "userId": self.user_id,
            "rcmdNum": 10,
            "pageNum": 1
        }
        res_text_T03 = request_post(url_T03, data_T03)
        try:
            res_dict_T03 = json.loads(res_text_T03)
            if res_dict_T03["code"] != 1000:
                case_message_T03 = {
                            "case_num": "T03",
                            "description": f'{self.path_code["T03"][1]}——接口响应异常',
                            "log": f"{res_text_T03}"
                        }
                SMS_message.append(case_message_T03)
            else:
                if len(res_dict_T03["recommendation"]) == 0:
                    case_message_T03 = {
                        "case_num": "T03",
                        "description": f'{self.path_code["T03"][1]}——推荐列表返回为空',
                        "log": f"{res_text_T03}"
                    }
                    SMS_message.append(case_message_T03)
                else:
                    pass
        except Exception as msg:
            case_message_T03 = {
                "case_num": "T03",
                "description": f'{self.path_code["T03"][1]}——服务响应异常',
                "log": f"{res_text_T03}"
            }
            SMS_message.append(case_message_T03)
            logger.error(f"系统异常记录:{case_message_T03}；报错信息：{msg}")

    def test004(self):
        """项目回放推荐结果查询接口"""
        url_T04 = f'{self.base_url}{self.path_code["T04"][0]}'
        data_T04 = {
            "userId": self.user_id,
            "rcmdNum": 10,
            "pageNum": 1
        }
        res_text_T04 = request_post(url_T04, data_T04)
        try:
            res_dict_T04 = json.loads(res_text_T04)
            if res_dict_T04["code"] != 1000:
                case_message_T04 = {
                    "case_num": "T04",
                    "description": f'{self.path_code["T04"][1]}——接口响应异常',
                    "log": f"{res_text_T04}"
                }
                SMS_message.append(case_message_T04)
            else:
                if len(res_dict_T04["recommendation"]) == 0:
                    case_message_T04 = {
                        "case_num": "T04",
                        "description": f'{self.path_code["T04"][1]}——推荐列表返回为空',
                        "log": f"{res_text_T04}"
                    }
                    SMS_message.append(case_message_T04)
                else:
                    pass
        except Exception as msg:
            case_message_T04 = {
                "case_num": "T04",
                "description": f'{self.path_code["T04"][1]}——服务响应异常',
                "log": f"{res_text_T04}"
            }
            SMS_message.append(case_message_T04)
            logger.error(f"系统异常记录:{case_message_T04}；报错信息：{msg}")

    def test005(self):
        """项目二级栏目推荐结果查询接口"""
        url_T08 = f'{self.base_url}{self.path_code["T08"][0]}'
        data_T08 = {
            "userId": self.user_id
        }
        res_text_T08 = request_post(url_T08, data_T08)
        try:
            res_dict_T08 = json.loads(res_text_T08)
            if res_dict_T08["code"] != 1000:
                case_message_T08 = {
                            "case_num": "T08",
                            "description": f'{self.path_code["T08"][1]}——接口响应异常',
                            "log": f"{res_text_T08}"
                        }
                SMS_message.append(case_message_T08)
            else:
                if len(res_dict_T08["recommendation"]) == 0:
                    case_message_T08 = {
                        "case_num": "T08",
                        "description": f'{self.path_code["T08"][1]}——推荐列表返回为空',
                        "log": f"{res_text_T08}"
                    }
                    SMS_message.append(case_message_T08)
                else:
                    # 执行T09接口
                    url_T09 = f'{self.base_url}{self.path_code["T09"][0]}'
                    data_T09 = {
                                "userId": self.user_id,
                                "tabId": res_dict_T08["recommendation"][0]["id"],
                                "rcmdNum": 50,
                                "pageNum": 1
                            }
                    res_text_T09 = request_post(url_T09, data_T09)
                    res_dict_T09= json.loads(res_text_T09)
                    if res_dict_T09["code"] != 1000:
                        case_message_T09 = {
                            "case_num": "T07",
                            "description": f'{self.path_code["T09"][1]}——接口响应异常',
                            "log": f"{res_text_T09}"
                        }
                        SMS_message.append(case_message_T09)
                    else:
                        pass
                        # if len(res_dict_T09["recommendation"]) == 0:
                        #     case_message_T09 = {
                        #         "case_num": "T09",
                        #         "description": f'{self.path_code["T09"][1]}——推荐列表返回为空',
                        #         "log": f"{res_text_T09}"
                        #     }
                        #     SMS_message.append(case_message_T09)
                        # else:
                        #     pass
        except Exception as msg:
            case_message = {
                "case_num": "T08/T09",
                "description": 'T08/T09接口——服务响应异常',
            }
            SMS_message.append(case_message)
            logger.error(f"系统异常记录:{case_message}；报错信息：{msg}")

    def test006(self):
        """视频推荐结果查询接口"""
        url_T10 = f'{self.base_url}{self.path_code["T10"][0]}'
        data_T10 = {
            "userId": self.user_id,
            "rcmdNum": 10,
            "pageNum": 1
        }
        res_text_T10 = request_post(url_T10, data_T10)
        try:
            res_dict_T10 = json.loads(res_text_T10)
            if res_dict_T10["code"] != 1000:
                case_message_T10 = {
                    "case_num": "T10",
                    "description": f'{self.path_code["T10"][1]}——接口响应异常',
                    "log": f"{res_text_T10}"
                }
                SMS_message.append(case_message_T10)
            else:
                if len(res_dict_T10["recommendation"]) == 0:
                    case_message_T10 = {
                        "case_num": "T10",
                        "description": f'{self.path_code["T10"][1]}——推荐列表返回为空',
                        "log": f"{res_text_T10}"
                    }
                    SMS_message.append(case_message_T10)
                else:
                    pass
        except Exception as msg:
            case_message_T10 = {
                "case_num": "T10",
                "description": f'{self.path_code["T10"][1]}——服务响应异常',
                "log": f"{res_text_T10}"
            }
            SMS_message.append(case_message_T10)
            logger.error(f"系统异常记录:{case_message_T10}；报错信息：{msg}")


if __name__ == '__main__':
    suite = unittest.TestSuite()  # 定义一个用例集合
    suite.addTest(MyTestCase('test001'))
    suite.addTest(MyTestCase('test002'))
    suite.addTest(MyTestCase('test003'))
    suite.addTest(MyTestCase('test004'))
    suite.addTest(MyTestCase('test005'))
    suite.addTest(MyTestCase('test006'))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    if SMS_message:  # 存在错误信息发送短信
        # for msg in SMS_message:
        #     if message:
        #         message = message + "；{}:{}".format(msg["case_num"], msg["description"])
        #     else:
        #         message = "【线上接口监控】{}:{}".format(msg["case_num"], msg["description"])
        # robot_data = {
        #                 "msgtype": "text",
        #                 "text": {
        #                     "content": SMS_message
        #                 }
        #             }
        robot_data = {
                        "msgtype": "text",
                        "text": {
                            "content": f"【线上接口监控异常消息】{json.dumps(SMS_message).encode('utf-8').decode('unicode_escape')}",
                            "mentioned_mobile_list": ["18637607203"]
                            # "mentioned_mobile_list": ["18637607203", "@all"]
                        }
                    }
        request_post(robot_url, robot_data)  # 发送企业微信信息
        logger.error("监控接口异常记录:{}".format(SMS_message))
    else:
        pass
