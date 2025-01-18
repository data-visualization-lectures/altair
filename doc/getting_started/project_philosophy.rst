プロジェクトの理念
==================

Python には、次のような優れたプロット・ライブラリが多数存在します:

* `Matplotlib <https://matplotlib.org/>`_
* `Bokeh <https://bokeh.pydata.org/en/latest/>`_
* `Seaborn <https://seaborn.pydata.org/>`_
* `Lightning <http://lightning-viz.org>`_
* `Plotly <https://plot.ly/>`_
* `pandas built-in plotting <https://pandas.pydata.org/pandas-docs/stable/visualization.html>`_
* `HoloViews <https://holoviews.org>`_
* `VisPy <https://vispy.org/>`_
* `pygg <https://www.github.com/sirrice/pygg>`_

各ライブラリは、特定の一連の処理をうまく実行します。

ユーザーの課題
---------------

しかし、このようなオプションの急増は、ユーザーにとって大きな困難をもたらします。

ユーザーは、これらの API のすべてを調べて、手元のタスクに最適なものを見つけなければなりません。これらのライブラリはどれも、高レベルの統計可視化に最適化されていないため、ユーザーはさまざまな API を組み合わせて独自のものを組み立てる必要があります。データ操作を学習しているばかりのユーザーにとっては、データの調査ではなく API の学習に集中せざるを得なくなります。

もう 1 つの課題は、現在のプロット API では、可視化の付随的な詳細であっても、ユーザーがコードを記述する必要があることです。これにより、可視化の種類 (ヒストグラム、散布図など) は、関心のある列やその列のデータ型などの基本情報を使用して推測できることが多いため、残念で不必要な認知的負担が生じます。

For example, if you are interested in the visualization of two numerical
columns, a scatterplot is almost certainly a good starting point. If you add
a categorical column to that, you probably want to encode that column using
colors or facets. If inferring the visualization proves difficult at times, a
simple user interface can construct a visualization without any coding.

たとえば、2 つの数値列の可視化に興味がある場合、散布図はほぼ間違いなく良い出発点です。これにカテゴリ列を追加する場合は、色またはファセットを使用してその列をエンコードする必要があります。可視化の推測が難しい場合は、シンプルなユーザー インターフェイスを使用して、コーディングなしで可視化を構築できます。以下のツールは、このような UI の優れた例です。

* `Tableau <https://www.tableau.com/>`_
* `Interactive Data Lab's <https://idl.cs.washington.edu/>`_
* `Polestar <https://github.com/vega/polestar>`_
* `Voyager <https://github.com/vega/voyager>`_

設計アプローチとソリューション
----------------------------

これらの課題は、プログラム API と組み込みレンダリングを備えた別の可視化ライブラリを作成しなくても解決できると考えています。
Vega-Altair の可視化構築アプローチでは、既存の可視化ライブラリの全機能を活用する階層化設計を採用しています:

1. 完全に宣言的な制約付きのシンプルな Python API (Vega-Altair) を作成する
2. API (Vega-Altair) を使用して、Vega-Lite 仕様に準拠した JSON 出力を生成する
3. 既存の可視化ライブラリを使用してその仕様をレンダリングする

このアプローチにより、ユーザーは最初ははるかにシンプルな API を使用して探索的な可視化を実行し、使用ケースに適したレンダラーを選択してから、そのレンダラーの全機能を活用してより高度なプロットのカスタマイズを行うことができます。

Matplotlib、Bokeh などの完全なプログラム API と比較すると、宣言型 API は必然的に制限されることを認識しています。これは、探索的可視化のユーザー エクスペリエンスを簡素化するために必要だと私たちは考えています。

Plotly と Altair のより詳細な比較については `this StackOverflow answer <https://stackoverflow.com/a/66040502>`_ をご覧ください。

