# brand-trend

SVMで極性評価した単語をもちいて、声優のポジティブネスをniconicoニュースコーパスを利用して、時系列的に表現します  

## もともとと起草
これは、もともともブランドの毀損などを評価しうるものとして、prophetなどの系列予想システムと連結させることで、急激なブランド毀損（炎上）などを検知して、炎上に対して適切な対応をとることにより、ブランドイメージを守ろうとするものでした(これは個人研究でやっていたのですが、どこにも引き取ってもらえないので、OSS、公開ナレッジ化します)　　

## Amazon, RakutenなどのレビューをコーパスにSVMなどで大規模極性辞書を作成する
もともとの意味のネガティブさ、ポジティブさというのはどのように評価すればいいのかわかりません。この時、SVMなどをレビュー情報（星の数）などを教師データに、極性を重んじた学習の分割が可能になります  

星の数を1,2,3個をネガティブとして、5個をポジティブとすると、非常にそれらしい結果が得ることができます。  


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
