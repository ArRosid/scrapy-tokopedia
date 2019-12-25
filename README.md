# scrapy-tokopedia
Scrapy project to scrape tokopedia.com

This is some features of this project
<ul>
  <li>
    To get all of promo, use this command<br>
    <b><i>scrapy crawl promo -o result_promo.json</i></b>
    <br><br>
    After get the json output, you can analyze the result using data science tool like pandas   
 
    >>> import pandas as pd
    >>> df = pd.read_json("result_promo.json")
    >>> df.head()
                                             description           periode minimum_transaction    promo_code
    0   Audio Year End Festival Cashback hingga Rp30.000       24 Des 2019           Rp150.000       HOMEAU3
    1  Dapatkan Diskon 50% sampai dengan Rp1.000.000 ...  18 - 31 Des 2019           Rp200.000    MAYAPADA50
    2  Fashion Pria & Wanita hingga Berbagai Aksesori...  23 - 29 Des 2019                              None
    3  Belanja Hemat Akhir Tahun di Tokopedia, Diskon...  20 - 25 Des 2019        Rp 1.000.000  DNMYEARENDCC
    4  Belanja Hemat Akhir Tahun, Diskon hingga Rp 15...  20 - 25 Des 2019          Rp 350.000  DNMYEARENDDB
  </li>
  <br>
  <li>
    To get best 10 of robotics book, you can use this command<br>
    <b><i>scrapy crawl best_10_robotic_books -o result_best_10_robotic_books.json</i></b>
    <br><br>
    After get the json output, you can analyze the result using data science tool like pandas   
 
    >>> import pandas as pd
    >>> df = pd.read_json("result_best_10_robotic_books.json")
    >>> 
    >>> df.head()
                                              book_title  book_price seller_location  rating  rating_count
    0  Buku Pintar Robotika, Merancang & Membuat Robo...  Rp 169.600     Kab. Sleman       5             3
    1                                           robotika   Rp 65.000   Jakarta Pusat       5             4
    2  ROBOTIKA  SENSOR DAN AKTUATOR   RIYANTO SIGIT ...   Rp 60.000         Bandung       5             2
    3  Buku Belajar Arduino itu Mudah! - Ebook Roboti...   Rp 29.900           Medan       5             2
    4          Buku Robotika - Teori dan Implementasinya   Rp 72.000   Jakarta Pusat       5             2
    >>> 
  </li>
  <br>
</ul>
