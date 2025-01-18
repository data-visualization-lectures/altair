.. _starting:

Basic Statistical Visualization
===================================

(This tutorial is adapted from `Vega-Lite's documentation
<http://vega.github.io/vega-lite/tutorials/getting_started.html>`_)

.. currentmodule:: altair

このチュートリアルでは、Altair で視覚化を作成する基本的なプロセスについて説明します。まず、Altair パッケージとその依存関係がインストールされていることを確認する必要があります (:ref:`インストール` を参照)。
このチュートリアルでは、プロットが自動的にレンダリングされるように、Jupyter ノートブック ユーザー インターフェイス (JupyterLab、Colab、VS Code など) 内で作業していることを前提としています。別のインターフェイスを使用している場合は、先に進む前に、Altair プロットの表示方法について読んでおくことをお勧めします (:ref:`チャートの表示` を参照)。

この基本的なチュートリアルの概要は次のとおりです:

- :ref:`basic-tutorial-data`
- :ref:`basic-tutorial-encodings-and-marks`
- :ref:`basic-tutorial-aggregation`
- :ref:`basic-tutorial-customization`
- :ref:`basic-tutorial-publishing`

.. _basic-tutorial-data:

The Data
--------

Data in Altair is built around the pandas Dataframe. One of the defining
characteristics of statistical visualization is that it begins with
`tidy <http://vita.had.co.nz/papers/tidy-data.html>`_
Dataframes. For the purposes of this tutorial, we'll start by importing pandas
and creating a simple DataFrame to visualize, with a categorical variable in
column a and a numerical variable in column b:

Altair のデータは、pandas Dataframe を中心に構築されています。統計視覚化の特徴の 1 つは、`tidy <http://vita.had.co.nz/papers/tidy-data.html>`_ なDataframes から始まることです。このチュートリアルでは、pandas をインポートし、列 a にカテゴリ変数、列 b に数値変数を含む、視覚化する単純な DataFrame を作成することから始めます。

.. altair-plot::
   :output: none

   import pandas as pd
   data = pd.DataFrame({'a': list('CCCDDDEEE'),
                        'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]})


Altair を使用する場合、データセットはデータフレームとして提供されるのが最も一般的です。
後で説明するように、データフレームのラベル付き列は、Altair でのプロットに不可欠な要素です。

.. _basic-tutorial-chart-object:

The Chart Object
----------------

Altair の基本オブジェクトは :class:`Chart` で、データフレームを 1 つの引数として受け取ります:

.. altair-plot::
    :output: none

    import altair as alt
    chart = alt.Chart(data)

ここまでで Chart オブジェクトを定義しましたが、データに対してチャートに *何か* を実行するように指示していません。これは次に説明します。

.. _basic-tutorial-encodings-and-marks:

Encodings and Marks
-------------------

このチャート オブジェクトが手元にあるので、データをどのように可視化するかを指定できます。
これはチャート オブジェクトの ``mark`` 属性を介して行われます。
この属性には ``Chart.mark_*`` メソッドを介してアクセスするのが最も便利です。
たとえば、:meth:`~Chart.mark_point` を使用して、データをポイントとして表示できます:


.. altair-plot::

    alt.Chart(data).mark_point()


ここでのレンダリングはデータセットの行ごとに 1 つのポイントで構成され、これらのポイントの位置をまだ指定していないため、すべてが互いに重なってプロットされます。

ポイントを視覚的に分離するには、さまざまな *エンコード チャネル* (略して *チャネル* ) をデータセットの列にマッピングできます。

たとえば、データの変数 ``a`` を、ポイントの x 軸の位置を表す ``x`` チャネルで *エンコード* できます。

これは、:meth:`Chart.encode` メソッドを使用して簡単に実行できます:


.. altair-plot::

    alt.Chart(data).mark_point().encode(
        x='a',
    )

``encode()`` メソッドは、列名でアクセスされるデータセット内の列に対するエンコード チャネル (``x``, ``y``, ``color``, ``shape``, ``size`` など) 間のキーと値のマッピングを構築します。

pandas データフレームの場合、Altair はマッピングされた列の適切なデータ型 (この場合は *名目* 値または順序なしのカテゴリ) を自動的に決定します。

1 つの属性でデータを分離しましたが、各カテゴリ内で重複する複数のポイントがまだあります。 ``"b"`` 列にマッピングされた ``y`` エンコード チャネルを追加して、これらをさらに分離しましょう:


.. altair-plot::

    alt.Chart(data).mark_point().encode(
        x='a',
        y='b'
    )


「b」列のデータの型は、再び Altair によって自動的に推測され、今回は *定量的* 型 (つまり、実数値) として扱われます。
さらに、グリッド線と適切な軸タイトルも自動的に追加されます。

.. _basic-tutorial-aggregation:

Data Transformation: Aggregation
--------------------------------

データの視覚化方法をより柔軟にするために、Altair にはデータの *集計* 用の組み込み構文があります。

たとえば、列識別子内でこの集計を指定することにより、すべての値の平均を計算できます:



.. altair-plot::

    alt.Chart(data).mark_point().encode(
        x='a',
        y='average(b)'
    )

これで、各 x 軸カテゴリ内に、そのカテゴリ内の値の平均を反映する 1 つのポイントが表示されます。

通常、集計値はポイント マークではなくバー マークで表されます。これを行うには、:meth:`~Chart.mark_point` を :meth:`~Chart.mark_bar` に置き換えます。


.. altair-plot::

    alt.Chart(data).mark_bar().encode(
        x='a',
        y='average(b)'
    )

カテゴリ特性は ``x`` 軸にマッピングされるため、結果は縦棒グラフになります。横棒グラフを作成するには、 ``x`` と ``y`` キーワードを入れ替えるだけです:

.. altair-plot::

    alt.Chart(data).mark_bar().encode(
        y='a',
        x='average(b)'
    )

Aside: Examining the JSON Output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Altair の主な目的は、プロット仕様を Vega-Lite スキーマに準拠する JSON 文字列に変換することであることを思い出してください。

ここでは、:meth:`~Chart.to_json` メソッドを使用して、Altair がエクスポートして Vega-Lite に JSON として送信している JSON 仕様を調べるのが有益です:


.. altair-plot::
    :output: stdout

    chart = alt.Chart(data).mark_bar().encode(
        x='a',
        y='average(b)',
    )
    print(chart.to_json())


ここで、``encode(x='a')`` が ``field`` 名とデータの ``type`` を持つ JSON 構造に展開されていることに注意してください。

``encode(y='b')`` も同様に展開されており、``aggregate`` フィールドが含まれています。

Altair の完全な省略構文には、列のタイプを指定する方法も含まれています:



.. altair-plot::
    :output: stdout

    y = alt.Y('average(b):Q')
    print(y.to_json())

この省略形は、パラメータを名前で綴ることと同じです:

.. altair-plot::
    :output: repr

    y = alt.Y(field='b', type='quantitative', aggregate='average')
    print(y.to_json())

このより詳細なチャネル指定方法は、Altair チャート仕様で直接使用できます。これは、より高度なフィールド構成を使用する場合に役立ちます:

.. altair-plot::

    alt.Chart(data).mark_bar().encode(
        alt.Y('a', type='nominal'),
        alt.X('b', type='quantitative', aggregate='average')
    )


.. _basic-tutorial-customization:

Customizing your Visualization
------------------------------

デフォルトでは、Altair は Vega-Lite を介して視覚化のデフォルト プロパティについていくつかの選択を行います。

Altair は視覚化の外観をカスタマイズするための API も提供します。

たとえば、チャネル クラスの :meth:`title` メソッドを使用して軸のタイトルを指定したり、 ``Chart.mark_*`` メソッドの ``color`` キーワードを任意の有効な HTML 色文字列に設定してマークの色を指定したりできます。

.. altair-plot::

    alt.Chart(data).mark_bar(color='firebrick').encode(
        alt.Y('a').title('category'),
        alt.X('average(b)').title('avg(b) by category')
    )


.. _basic-tutorial-publishing:

Publishing your Visualization
-----------------------------

データを可視化したら、それを Web 上のどこかに公開したいと考えるかもしれません。これは、Vega-Embed_ Javascript パッケージを使用して簡単に実行できます。

:meth:`Chart.save` メソッドを使用して、任意のチャートのスタンドアロン HTML ドキュメントの簡単な例を生成できます。

.. code-block:: python

    chart = alt.Chart(data).mark_bar().encode(
        x='a',
        y='average(b)',
    )
    chart.save('chart.html')

基本的な HTML テンプレートは次のような出力を生成します。:meth:`Chart.to_json` によって生成されたプロットの JSON 仕様は ``spec`` Javascript 変数に保存される必要があります:

.. code-block:: html

  <!DOCTYPE html>
  <html>
    <head>
      <script src="https://cdn.jsdelivr.net/npm/vega@3"></script>
      <script src="https://cdn.jsdelivr.net/npm/vega-lite@2"></script>
      <script src="https://cdn.jsdelivr.net/npm/vega-embed@3"></script>
    </head>
    <body>
      <div id="vis"></div>
      <script type="text/javascript">
        var spec = {};  /* JSON dump of your chart's spec */
        var opt = {"renderer": "canvas", "actions": false};  /* Options for the embedding */
        vegaEmbed("#vis", spec, opt);
      </script>
    </body>
  </html>

:meth:`~Chart.save` メソッドは、このような HTML 出力をファイルに保存する便利な方法を提供します。

Altair/Vega-Lite の埋め込みの詳細については、Vega-Embed_ プロジェクトのドキュメントを参照してください。

.. _Vega-Embed: https://github.com/vega/vega-embed
