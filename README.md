# Latex_Basic_Generation
<div style="text-align: justify"> Fairly simple Python script to join figures and tables and generate a basic LaTeX report code in order to save some valuable minutes of life.</div>

## How to use:

<div style="text-align: justify"> Just call the `build_latex_report()` function as shown in the example `test_builder.py`:</div>

	report_title = 'Report: Lorenz Attractor'
	report_date = 'Oct 2019'
	logo_path = 'randomlogo.jpg'
	pictures_folder = 'Report_Figures'
	tables_folder = 'Report_Tables'
	dic_capt_figures = {'fig_1_lorenz_' : 'Lorenz attractor.'}
	dic_capt_tables = {'tab_1_lorenzparams_' : 'Lorenz parameters.'}
	keyname_order = ['tab_1_lorenzparams_', 'fig_1_lorenz_']
	outdocument_path = 'Report_Lorenz.tex'
	build_latex_report( report_title, report_date, logo_path, outdocument_path, pictures_folder, dic_capt_figures, tables_folder, dic_capt_tables, keyname_order )

<div style="text-align: justify"> All figures must be located on a folder `pictures_folder`, while all the tables must be text files located on `tables_folder`. Note that each table file can be easily created with the Pandas `.to_latex()` method and exporting the output string as a `.txt` file.</div>

<div style="text-align: justify"> `dic_capt_figures` and `dic_capt_tables` are dictionaries containing the name of each figure and table respectively as keys and their corresponding captions as values. `keyname_order` is just a list of the elements to put in the `.tex` file and their order. `outdocument_path` is the name of the output file to generate.</div>

<div style="text-align: justify"> After generating the `.tex` file, run it on a LaTeX interpreter application to keep working on the document and build the output PDF.</div>
