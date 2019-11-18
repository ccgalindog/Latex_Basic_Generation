# Latex_Basic_Generation
Fairly simple Python script to join figures and tables and generate a basic LaTeX report code in order to save some valuable minutes of life.

## How to use:

Just call the `build_latex_report()` function as shown in test_builder.py.

	report_title = 'Report: Lorenz Attractor'
	report_date = 'Oct 2019'
	logo_path = 'randomlogo.jpg'
	pictures_folder = 'Report_Figures'
	tables_folder = 'Report_Tables'
	dic_capt_figures = {'fig_1_lorenz_' : 'Lorenz attractor.'}
	dic_capt_tables = {'tab_1_lorenzparams_' : 'Lorenz parameters.'}
	keyname_order = ['tab_1_lorenzparams_', 'fig_1_lorenz_']
	outdocument_path = 'Report_Lorenz.tex'
	build_latex_report( report_title, report_date, logo_path, outdocument_path, pictures_folder, dic_capt_figures, tables_folder, 					dic_capt_tables, keyname_order )

