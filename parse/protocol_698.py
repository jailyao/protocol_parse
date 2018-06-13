class Pro_69845_Parse:
    def ParseFrame(self, frame):
        index = 0
        default_result = '\0' + '698.45 -- 解析结果如下：\n*********************************\n'
        end_result = '*********************************\n解析结束！\n'
        result = default_result
        for data in frame:
            result += '%02X ' % data
        result += '\n'
        result += end_result
        return result