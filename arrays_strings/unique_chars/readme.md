## 単語で同じキャラクターが使われているか？

3つのアルゴリズムを利用する。
- Algorithm 1: Sets and Length Comparison : UniqueCharsSet()
- Algorithm 2: Hash Map Lookup : UniqueChars()
- Algorithm 3: In-Place : UniqueCharsInPlace()


1. Algorithm 1: Sets and Length Comparison
   pythonのset()を利用する
2. Algorithm 2: Hash Map Lookup
   ハッシュテーブル or ハッシュマップ。ウィキペディアによれば、[ハッシュテーブル (英: hash table) は、キーと値の組（エントリと呼ぶ）を複数個格納し、キーに対応する値をすばやく参照するためのデータ構造。][20]。
3. Algorithm 3: In-Place
   ウィキペディアによれば、[in-placeアルゴリズムとは、計算機科学においてデータ構造の変換を行うにあたって、追加の記憶領域をほとんど使わずに行うアルゴリズムを意味する。][21]。図が提示されている例では、keys / indexes / key-value pairsの構成となっているが。今回は重複確認なのでindexexパートまでとなる。
   pythonの[組み込み型のページ][22]を"重複"で検索しcount()が使えることがわかる。
   
[20]:https://ja.wikipedia.org/wiki/%E3%83%8F%E3%83%83%E3%82%B7%E3%83%A5%E3%83%86%E3%83%BC%E3%83%96%E3%83%AB   
[21]:https://ja.wikipedia.org/wiki/In-place%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0
[22]:https://docs.python.org/ja/3/library/stdtypes.html?highlight=count#string-methods