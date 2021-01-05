import re

content = """
 <dl class="consent">

          <dt class="purple">演奏</dt>
          <dd class="txt">
          <p>この利用分野は、JASRACが著作権を管理しています。</p>



        </dd>
      </dl>
      <section class="content-block">
        <div class="title">
          管理状況詳細

          <div class="ico purple">演奏</div>

          <a href="" class="btn-acd"></a>
        </div>
        <div class="content">

          <!-- PC表示 -->
          <div class="PC">
            <table class="detail">
              <tbody><tr>
                <th colspan="4">著作者/出版者情報</th>
                <th colspan="2">管理情報</th>
              </tr>

              <tr>
                <th>No.</th>
                <th>
                  著作者/出版者<a href="help/help_words.html#ip" target="_blank" class="ico_info"></a>
                </th>
                <th>
                  識別<a href="help/help_words.html#iprole" target="_blank" class="ico_info"></a>
                </th>
                <th>
                  契約<a href="help/help_words.html#contract" target="_blank" class="ico_info"></a>
                </th>
                <th>
                  所属団体<a href="help/help_words.html#societyorganization" target="_blank" class="ico_info"></a>
                </th>
                <th>特記<a href="help/help_words.html#specialmention" target="_blank" class="ico_info"></a></th>
              </tr>



            <!-- 著作者/出版社がPD or 分配率ハイフン or 特記欄「-」マークが表示されてるとき、背景グレー -->

            <tr>

                <td class="center">1</td>
                <td>GEIGER TEDDY</td>
                <td class="center">作曲作詞</td>

                	<td class="center">&nbsp;</td>

                <td class="center">






                			演奏:BMI<br>録音:-<br>



                </td>
                <td class="detail-tokki">






                </td>
                </tr>



            <!-- 著作者/出版社がPD or 分配率ハイフン or 特記欄「-」マークが表示されてるとき、背景グレー -->

            <tr>

                <td class="center">2</td>
                <td>KYRIAKIDES DANIEL JOHN</td>
                <td class="center">作曲作詞</td>

                	<td class="center">&nbsp;</td>

                <td class="center">






                			演奏:BMI<br>録音:-<br>



                </td>
                <td class="detail-tokki">






                </td>
                </tr>



            <!-- 著作者/出版社がPD or 分配率ハイフン or 特記欄「-」マークが表示されてるとき、背景グレー -->

            <tr>

                <td class="center">3</td>
                <td>PARKER DANNY</td>
                <td class="center">作曲作詞</td>

                	<td class="center">&nbsp;</td>

                <td class="center">






                			演奏:BMI<br>録音:-<br>



                </td>
                <td class="detail-tokki">






                </td>
                </tr>



            <!-- 著作者/出版社がPD or 分配率ハイフン or 特記欄「-」マークが表示されてるとき、背景グレー -->

            <tr>

                <td class="center">4</td>
                <td>MUSIC OF BIG DEAL 302</td>
                <td class="center">出版者&nbsp;</td>

                	<td class="center">&nbsp;</td>

                <td class="center">






                			演奏:BMI<br>録音:-<br>



                </td>
                <td class="detail-tokki">






                </td>
                </tr>



            <!-- 著作者/出版社がPD or 分配率ハイフン or 特記欄「-」マークが表示されてるとき、背景グレー -->

            <tr>

                <td class="center">&nbsp;</td>
                <td>ピアーミュージック</td>
                <td class="center">サブ出版</td>

                	<td class="center">&nbsp;</td>

                <td class="center">



                		JASRAC


                </td>
                <td class="detail-tokki">






                </td>
                </tr>


            </tbody></table>
          </div>
          <!-- END PC表示 -->
                    <!-- SP表示 -->
          <div class="SP">




            <table class="detail">



            		<tbody><tr>

            		<th colspan="3">No.1</th>
            		</tr>



            <tr>

                <th colspan="2">著作者/出版者<a href="help/help_words.html#ip" target="_blank" class="ico_info"></a></th>
                <td>GEIGER TEDDY</td>
              </tr>


            <tr>

                <th rowspan="2">著作者<span>/</span>出版者情報</th>
                <th>識別<a href="help/help_words.html#iprole" target="_blank" class="ico_info"></a></th>
                <td>作曲作詞</td>
              </tr>


            <tr>

                <th>契約<a href="help/help_words.html#contract" target="_blank" class="ico_info"></a></th>

                	<td>&nbsp;</td>

              </tr>


            <tr>

                <th rowspan="2">管理情報</th>
                <th>所属団体<a href="help/help_words.html#societyorganization" target="_blank" class="ico_info"></a></th>

                	<td>





                			演奏:BMI<br>録音:-<br>


                	</td>

              </tr>


            <tr>

                <th>特記<a href="help/help_words.html#specialmention" target="_blank" class="ico_info"></a></th>
                <td class="detail-tokki">






                </td>
                </tr>

                </tbody></table>


            <table class="detail">



            		<tbody><tr>

            		<th colspan="3">No.2</th>
            		</tr>



            <tr>

                <th colspan="2">著作者/出版者<a href="help/help_words.html#ip" target="_blank" class="ico_info"></a></th>
                <td>KYRIAKIDES DANIEL JOHN</td>
              </tr>


            <tr>

                <th rowspan="2">著作者<span>/</span>出版者情報</th>
                <th>識別<a href="help/help_words.html#iprole" target="_blank" class="ico_info"></a></th>
                <td>作曲作詞</td>
              </tr>


            <tr>

                <th>契約<a href="help/help_words.html#contract" target="_blank" class="ico_info"></a></th>

                	<td>&nbsp;</td>

              </tr>


            <tr>

                <th rowspan="2">管理情報</th>
                <th>所属団体<a href="help/help_words.html#societyorganization" target="_blank" class="ico_info"></a></th>

                	<td>





                			演奏:BMI<br>録音:-<br>


                	</td>

              </tr>


            <tr>

                <th>特記<a href="help/help_words.html#specialmention" target="_blank" class="ico_info"></a></th>
                <td class="detail-tokki">






                </td>
                </tr>

                </tbody></table>


            <table class="detail">



            		<tbody><tr>

            		<th colspan="3">No.3</th>
            		</tr>



            <tr>

                <th colspan="2">著作者/出版者<a href="help/help_words.html#ip" target="_blank" class="ico_info"></a></th>
                <td>PARKER DANNY</td>
              </tr>


            <tr>

                <th rowspan="2">著作者<span>/</span>出版者情報</th>
                <th>識別<a href="help/help_words.html#iprole" target="_blank" class="ico_info"></a></th>
                <td>作曲作詞</td>
              </tr>


            <tr>

                <th>契約<a href="help/help_words.html#contract" target="_blank" class="ico_info"></a></th>

                	<td>&nbsp;</td>

              </tr>


            <tr>

                <th rowspan="2">管理情報</th>
                <th>所属団体<a href="help/help_words.html#societyorganization" target="_blank" class="ico_info"></a></th>

                	<td>





                			演奏:BMI<br>録音:-<br>


                	</td>

              </tr>


            <tr>

                <th>特記<a href="help/help_words.html#specialmention" target="_blank" class="ico_info"></a></th>
                <td class="detail-tokki">






                </td>
                </tr>

                </tbody></table>


            <table class="detail">



            		<tbody><tr>

            		<th colspan="3">No.4</th>
            		</tr>



            <tr>

                <th colspan="2">著作者/出版者<a href="help/help_words.html#ip" target="_blank" class="ico_info"></a></th>
                <td>MUSIC OF BIG DEAL 302</td>
              </tr>


            <tr>

                <th rowspan="2">著作者<span>/</span>出版者情報</th>
                <th>識別<a href="help/help_words.html#iprole" target="_blank" class="ico_info"></a></th>
                <td>出版者&nbsp;</td>
              </tr>


            <tr>

                <th>契約<a href="help/help_words.html#contract" target="_blank" class="ico_info"></a></th>

                	<td>&nbsp;</td>

              </tr>


            <tr>

                <th rowspan="2">管理情報</th>
                <th>所属団体<a href="help/help_words.html#societyorganization" target="_blank" class="ico_info"></a></th>

                	<td>





                			演奏:BMI<br>録音:-<br>


                	</td>

              </tr>


            <tr>

                <th>特記<a href="help/help_words.html#specialmention" target="_blank" class="ico_info"></a></th>
                <td class="detail-tokki">






                </td>
                </tr>

                </tbody></table>


            <table class="detail">




            <tbody><tr>

                <th colspan="2">著作者/出版者<a href="help/help_words.html#ip" target="_blank" class="ico_info"></a></th>
                <td>ピアーミュージック</td>
              </tr>


            <tr>

                <th rowspan="2">著作者<span>/</span>出版者情報</th>
                <th>識別<a href="help/help_words.html#iprole" target="_blank" class="ico_info"></a></th>
                <td>サブ出版</td>
              </tr>


            <tr>

                <th>契約<a href="help/help_words.html#contract" target="_blank" class="ico_info"></a></th>

                	<td>&nbsp;</td>

              </tr>


            <tr>

                <th rowspan="2">管理情報</th>
                <th>所属団体<a href="help/help_words.html#societyorganization" target="_blank" class="ico_info"></a></th>

                	<td>


                		JASRAC

                	</td>

              </tr>


            <tr>

                <th>特記<a href="help/help_words.html#specialmention" target="_blank" class="ico_info"></a></th>
                <td class="detail-tokki">






                </td>
                </tr>

                </tbody></table>

          </div>
          <!-- END SP表示 -->
      </div>
    </section>

"""

th_re = re.compile(r'<td[^>]*>(.+)</td>')
th_span_re = re.compile(r'<td[^>]+>[^>]+>([^<]+)</span>[^<]*?</td>')


def parse(ctn: str):
    __table = []
    for item in ctn.split("</tr>"):
        datum = th_re.findall(item)
        if datum:
            __table.append(list(map(lambda x: str(x).strip().replace('&nbsp;', ' '), datum)))
    extra = {}
    for item in __table:
        if len(item) != 4:
            continue
        _, v, k, _ = item
        if k not in extra:
            extra[k] = []
        extra[k].append(v)
    return extra


data2 = """<table class="search-result">
      <tbody><tr>
        <th>内外</th>
        <th>作品コード</th>
        <th>作品タイトル</th>

  
        <th>著作者名</th>
  
  
  
  

        <th>アーティスト名</th>
        <th></th>
      </tr>

    

        

        <tr>
            <td data-role="result-naigai" class="center">
              <span class="txt">内</span>
            </td>
            <td data-role="result-code" class="center">
              <span>058-9437-9</span>
            </td>
            <td data-role="result-title">
             <span>愛だったんだよ</span>
            </td>

  
            <td data-role="result-author">
              <span>玉置　浩二</span>
            </td>
  
  
  
  

            <td data-role="result-artist">
              <span>玉置　浩二</span>
            </td>
            <td><a href="main?trxID=F20101&amp;WORKS_CD=05894379&amp;subSessionID=001&amp;subSession=start" target="_blank" class="btn btn-detail AUTO_JUMP">詳細</a></td>
        </tr>

    

    </tbody></table>
"""


def parse_header(ctn: str):
    __table = []
    for item in ctn.split("</tr>"):
        datum = th_span_re.findall(item)
        if datum:
            return list(map(
                lambda x: str(x).strip().replace('\u3000', ' '), datum))
    return __table


if __name__ == '__main__':
    print(parse(content))
