.. currentmodule:: altair

.. _installation:

インストール
============

Altair は、オプションの依存関係すべてとともに、次のコマンドを使用してインストールできます:

.. code-block:: bash

    pip install "altair[all]"

conda_ パッケージ マネージャーを使用している場合は、次のようになります:

.. code-block:: bash

    conda install -c conda-forge altair-all


この時点で、Jupyter Notebook と互換性のある任意の IDE を開いて、:ref:`example-gallery` のコードを実行できるはずです。
さまざまなノートブック環境およびノー​​トブック以外の IDE でチャートを表示する方法の詳細については、:ref:`displaying-charts` を参照してください。
必要な依存関係のみを使用して Altair をインストールする場合は  ``[all]``/``-all`` サフィックスを省略できます。
次のものを使用して、チャートをオフライン HTML ファイルまたは PNG/SVG/PDF 形式で保存するために必要な依存関係のみを使用して Altair をインストールすることもできます。

Altair は、次のものを使用して、チャートをオフライン HTML ファイルまたは PNG/SVG/PDF 形式で保存するために必要な依存関係のみをインストールすることもできます:

.. code-block:: bash

    pip install "altair[save]"

開発インストール
========================

Altair プロジェクトへの貢献方法の詳細については  `CONTRIBUTING.md <https://github.com/vega/altair/blob/main/CONTRIBUTING.md>`_ を参照してください。


.. _conda: https://docs.conda.io/
.. _Vega-Lite: http://vega.github.io/vega-lite
.. _vega_datasets: https://github.com/altair-viz/vega_datasets
.. _JupyterLab: http://jupyterlab.readthedocs.io/
.. _Jupyter Notebook: https://jupyter-notebook.readthedocs.io/
