from parse import common_interface

class Pro_104_Parse:
    def ParseFrame(self, frame):
        index = 0
        default_result = '\0'+'104 -- 解析结果如下：\n*********************************\n'
        end_result = '*********************************\n解析结束！\n'
        content_result = ''
        i_frame_info = []  # APDU_LEN + TI + VSQ + COT
        if frame[0] != 0x68:
            result = default_result + '输入帧非法：帧头非法！\n' + end_result
            return result
        else:
            frame_len = frame[1]
            if (frame_len < 4) or (frame_len > (len(frame) - 2)):
                result = default_result + 'APDU总长度非法或者帧不完整！\n' + end_result
                return result
            result = default_result + 'APDU总长度为: ' + '%d' % frame_len + '\n'
            i_frame_info.append(frame_len)  # append length of APDU
        index += 2   # head & length
        frame_info = self.GetFrameInfo(frame, index)
        index += 4   # control area
        if frame_info[0] is 'Unknow':
            result = default_result + '帧类型非法！\n' + end_result
            return result
        else:
            result += '帧类型： ' + frame_info[0] + '\n'
        if frame_info[0] is 'type_U':
            result += '功能类型: ' + frame_info[1] + '\n'
        else:
            result += '发送帧数量: ' + '%d' % frame_info[2] + '\n'
            result += '接收帧数量: ' + '%d' % frame_info[3] + '\n'
        if frame_info[0] is not 'type_I':
            result += (content_result + end_result)
            return result
        result += 'I帧内容如下：\n' + '------------------------\n'
        if frame[index] not in common_interface.type_id_dic:
            result = default_result + 'TypeID非法！\n' + end_result
            return result
        else:
            result += 'TI: ' + common_interface.type_id_dic[frame[index]] + '\n'
            i_frame_info.append(frame[index])
        result += 'VSQ: ' + '%02X' % frame[index+1] + '\n'
        result += '信息体个数为： ' + '%d' % (frame[index+1] & 0x7f) + '\n'
        i_frame_info.append(frame[index+1])
        index += 2
        if (frame[index] + frame[index+1]*16) not in common_interface.cot_dic:
            result = default_result + 'COT非法！\n' + end_result
            return result
        else:
            result += 'COT: ' + common_interface.cot_dic[frame[index] + frame[index+1]*16] + '\n'
            i_frame_info.append(frame[index] + frame[index+1]*16)
        index += 2
        pub_addr = frame[index] + frame[index+1]*16
        if pub_addr is not pub_addr:
            result = default_result + '公共地址非法！\n' + end_result
            return result
        result += 'Public Address: ' + '%d' % pub_addr + '(%02X %02X)' % (frame[index], frame[index+1]) + '\n'
        index += 2
        content_result = self.Parse_104_Content(frame, index, i_frame_info)
        result += (content_result + end_result)
        return result

    def GetFrameInfo(self, data, index):
        frame_info = []
        fun_type_dic = {0x04: 'StartEnable', 0x08: 'StartConfirm', 0x10: 'StopEnable', \
                        0x20: 'StopConfirm', 0x40: 'TestEnable', 0x80: 'TestConfirm'}
        if (data[index] & 0x01) is 0:  # type I
            SendCnt = (((data[index+1] << 8) + (data[index] & 0xFE)) >> 1)
            RcvCnt = (((data[index+3] << 8) + (data[index+2] & 0xFE)) >> 1)
            frame_info.append('type_I')
            frame_info.append('Unknow')
            frame_info.append(SendCnt)
            frame_info.append(RcvCnt)
        elif (data[index] & 0x03) is 1:  # type S
            RcvCnt = (((data[index+3] << 8) + (data[index+2] & 0xFE)) >> 1)
            frame_info.append('type_S')
            frame_info.append('Unknow')
            frame_info.append(0)
            frame_info.append(RcvCnt)
        elif (data[index] & 0x03) is 0x03:  # type U
            u8Tmp = data[index] & 0xFC
            frame_info.append('type_U')
            if u8Tmp not in fun_type_dic:
                frame_info.append('Unknow')
            else:
                frame_info.append(fun_type_dic[u8Tmp])
            frame_info.append(0)
            frame_info.append(0)
        else:
            frame_info.append('Unknow')
            frame_info.append('Unknow')
            frame_info.append(0)
            frame_info.append(0)
        return frame_info

    def Parse_104_Content(self, frame, index, i_frame_info):
        content = ''
        if i_frame_info[0] < 10:
            content = 'I帧长度非法！\n'
            return content
        content_len = i_frame_info[0] - 10
        content = 'I帧的数据内容如下：-->\n'
        for i in range(content_len):
            content += '%02X ' % frame[index+i]
        content += '\n'
        return content


