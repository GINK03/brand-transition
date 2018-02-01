# brand-trend

SVMで極性評価した単語をもちいて、声優のポジティブネスをniconicoニュースコーパスを利用して、時系列的に表現します  

## もともとと起草
これは、もともともブランドの毀損などを評価しうるものとして、prophetなどの系列予想システムと連結させることで、急激なブランド毀損（炎上）などを検知して、炎上に対して適切な対応をとることにより、ブランドイメージを守ろうとするものでした(これは個人研究でやっていたのですが、どこにも引き取ってもらえないので、OSS、公開ナレッジ化します)　　

## Amazon, RakutenなどのレビューをコーパスにSVMなどで大規模極性辞書を作成する
もともとの意味のネガティブさ、ポジティブさというのはどのように評価すればいいのかわかりません。この時、SVMなどをレビュー情報（星の数）などを教師データに、極性を重んじた学習の分割が可能になります  

星の数を1,2,3個をネガティブとして、5個をポジティブとすると、非常にそれらしい結果が得ることができます。  

### 学習した結果のウェイト
negative度が高いもの
```console
売り手 -4.393270938125656
ガッカリ -3.947897992103171
がっかり -3.648103587594949
残念 -3.130127382290406
致命 -3.112032623756082
期待はずれ -3.083929660401355
返品 -2.948516584384151
灰皿 -2.87787780959521
３つ -2.783511547585251
駄作 -2.771137686778778
物足りなかっ -2.663694159049179
最悪 -2.655338531812268
うーん -2.499197140760456
二度と -2.480062770645911
意味不明 -2.420151065200296
いまいち -2.419859090879487
失せ -2.41635935742869
つまらない -2.404018144393537
単調 -2.368271765218191
堀江 -2.34675269334997
つまらなかっ -2.316511096716675
タートル -2.288030642964168
イマイチ -2.27754859957102
目新しい -2.269002906892812
まずい -2.23071763111786
欠ける -2.222289341852733
...
```
positive度が高いもの
```console
お買い得 1.987645060840108
最高傑作 1.990702627997584
別格 2.011164421643425
目からウロコ 2.014549379784212
これ程 2.019119980229243
杞憂 2.026934292869131
戻れ 2.052378639149482
オジさん 2.061753308187434
痛快 2.061960603545156
欠か 2.087942969787786
叩け 2.08933 2.130187229517098
pop 2.1307765382222862
病みつき 2.142924963400594
憎め 2.160722430925575
洋楽 2.169574554504112
強いて 2.224321728820268
バイブル 2.229368722596254
絶妙 2.245596441611436
従う 2.254309352677592
五つ 2.255604793487576
待ち遠しい 2.25806614954727
逸品 2.265821501069568
最高 2.289466171874273
傑作 2.293924930835376
サウンドトラック 2.295214513832636
是非 2.311342110589227
半信半疑 2.39707658523505
ガル2.661651342883942922
R&B 2.6851915989280470909009
一括 2.730196185564076
リッツ 2.766706018272894
大正解 2.874333983897774
手放せ 2.948887203551322
必読 3.012749694663035
セレクトショップ 3.050995942436786
５つ 3.081741024496506
秀逸 3.229761176207314
...
```
このようにそれらしい結果が得られます 

## ある人名が含まれているドキュメントが含まれているドキュメントのネガポジをその語の含まれている文脈の意味とする

## 時系列的にドキュメントを並べて、ある人名のポジティブ度をSVMで作成した重みを利用して時系列順に並べる


## 実験結果

<p align="center">
  <img width="550px" src="https://user-images.githubusercontent.com/4949982/35660588-453a1264-0750-11e8-904f-3593081fb1e6.png">
</p>
<div align="center"> 図1. 早見沙織の時系列データ </div>

<p align="center">
  <img width="550px" src="https://user-images.githubusercontent.com/4949982/35660883-1e6ecc18-0752-11e8-96f2-450e3d5bbfa0.png">
</p>
<div align="center"> 図2. 水瀬いのりの時系列データ </div>

<p align="center">
  <img width="550px" src="https://user-images.githubusercontent.com/4949982/35662731-0ee4d200-075d-11e8-9581-b3288eb9b878.png">
</p>
<div align="center"> 図3. 日笠陽子の時系列データ </div>
