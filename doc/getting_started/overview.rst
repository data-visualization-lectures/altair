.. _overview:

Overview
========

Vega-Altair は、Vega_ および Vega-Lite_ をベースにした、Python 用の宣言型統計可視化ライブラリです。

強力で簡潔な文法を提供し、幅広い統計可視化をすばやく構築できます。以下は、API を使用してインタラクティブな散布図でデータセットを視覚化する例です:

.. altair-plot::

    # import altair with an abbreviated alias
    import altair as alt

    # load a sample dataset as a pandas DataFrame
    from vega_datasets import data
    cars = data.cars()

    # make the chart 
    alt.Chart(cars).mark_point().encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
    ).interactive()

重要なアイデアは *データ列* と *視覚エンコーディング チャネル* (x 軸、y 軸、色など) の間のリンクを宣言することです。プロットの残りの詳細は自動的に処理されます。この宣言型システムを基に、簡潔な文法を使用して、シンプルなものから高度なものまで、驚くほど幅広いプロットを作成できます。

このプロジェクトは、わし座の `最も明るい星(Altair) <https://en.wikipedia.org/wiki/Altair>`_ にちなんで名付けられました。地球の空から見ると、Altair は、親プロジェクトの名前の由来となった星である Vega の近くに見えます。

このドキュメントは、Altair を学習するための主なリファレンスとして機能します。追加の学習資料とチュートリアルは :ref:`learning-resources` セクションにあります。`Vega-Lite ドキュメント <https://vega.github.io/vega-lite/docs/>`_ を参照することも役立ちます。


.. _Vega: http://vega.github.io/vega
.. _Vega-Lite: http://vega.github.io/vega-lite


.. toctree::
   :maxdepth: 1
   :caption: Getting Started
   :hidden:

   self
   installation
   starting
   getting_help
   resources
   project_philosophy
