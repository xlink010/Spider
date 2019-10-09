import codecs

class   DataOutput(object):

    def __init__(self):
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('koubei.html', 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'/><head>")
        fout.write("<body>")
        fout.write("<table>")
        fout.write("<tr>")
        fout.write("<td>网站<td/>")
        fout.write("<td>时间<td/>")
        fout.write("<td>评分<td/>")
        fout.write("<td>用户<td/>")
        fout.write("<td>评论<td/>")
        fout.write("</tr>")
        if (self.datas is None) or (len(self.datas) == 0):
            print("error")
        else:
            for data in self.datas:
                for element in zip(data['time'], data['score'], data['user_name'], data['comment']):
                    fout.write("<tr>")
                    fout.write("<td>%s<td/>" % data['url'])
                    fout.write("<td>%s<td/>" % element[0])
                    fout.write("<td>%s<td/>" % element[1])
                    fout.write("<td>%s<td/>" % element[2])
                    fout.write("<td>%s<td/>" % element[3])
                    fout.write("</tr>")
                    #self.datas.remove(data)
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()