class Pro_13761_Parse:
    def ParseFrame(self, frame):
        index = 0
        cs = 0
        default_result = '\0' + '1376.1 -- 解析结果如下：\n*********************************\n'
        end_result = '*********************************\n解析结束！\n'
        result = default_result
        # check frame head & tail
        tmp_result = self.ParseFrmHead(frame, index)
        if tmp_result[0] is 0:
            result = default_result + tmp_result[1] + end_result
            return result
        result += tmp_result[1]
        index += 6   # 68 + L + L +68
        # check CRC
        for i in range(tmp_result[0]):
            cs += frame[i+index]
        if (cs & 0xff) != frame[index + tmp_result[0]]:
            result = default_result + '校验位错误：应为' + '%02X' % (cs & 0xff) + '\n' + end_result
            return result

        # check Ctrl and address
        result += '控制码：' + '%02X' % frame[index] + '\n'
        index += 1
        result += '地址域：' + '%02X %02X %02X %02X %02X' % \
                           (frame[index], frame[index+1], frame[index+2], frame[index+3], frame[index+4]) + '\n'
        index += 5

        # check AFN & SEQ
        result += 'AFN:' + '%02X' % frame[index] + '\n'
        result += 'SEQ:' + '%02X' % frame[index+1] + '\n'
        index += 2

        # check data content
        result += '----------------------------\n数据内容如下：\n'
        for i in range(tmp_result[0]-8):
            result += '%02X ' % frame[index+i]
        result += '\n----------------------------\n'
        result += end_result
        return result


    def ParseFrmHead(self, frame, index):
        ret_result = []
        if (frame[index] is not 0x68) or (frame[index + 5] is not 0x68):
            ret_result.append(0)
            ret_result.append('输入帧非法:帧头错误！\n')
            return ret_result
        apdu_len = (((frame[index+2] << 8) + frame[index+1]) >> 2)
        input_len = len(frame)
        if (frame[index+1] != frame[index+3]) or\
                (frame[index+2] != frame[index+4]) or\
                ((apdu_len+8) > input_len):
            ret_result.append(0)
            ret_result.append('输入帧非法:长度错误或者帧不完整！\n')
            return ret_result
        if frame[index+apdu_len+7] is not 0x16:
            ret_result.append(0)
            ret_result.append('输入帧非法:结束符错误！\n' + '%d - %02x' % (index+apdu_len+7, frame[index+apdu_len+7]))
            return ret_result
        ret_result.append(apdu_len)
        ret_result.append('用户数据区长度：' + '%d' % apdu_len + '\n')
        return ret_result