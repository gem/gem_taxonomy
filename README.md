# GEM BUILDING TAXONOMY

The GEM Building Taxonomy is a uniform classification scheme, a method for describing and categorising buildings in the same way across the globe as a key step towards assessing their vulnerability and risk. The taxonomy provides a language model that characterises assets according to attributes that can influence the likelihood of damage due to the effects of natural hazards.

The `GEM Building taxonomy v3.3` contains 13 building attributes, including the main material of construction, lateral load-resisting system, date of construction and number of storeys. This repository provides the spreadsheets with the latest attributes.

[Taxonomy_tables_v3.3.xlsx](./Taxonomy_tables_v3.3.xlsx)

![taxonomy_v3.3](figures/taxonomy_v3.3.png)

## Applications

### Validate and explain taxonomy strings
If you want to validate a taxonomy string or better understand its meaning, you can use the taxonomy validation and explanation tool:

https://tools.openquake.org/taxonomy/
<br>
<br> 

![Taxonomy tool](figures/taxonomy_tool.png)


### Python package

For engineers and scientists working with the taxonomy for model or tool development, the following Python package validates taxonomy strings, provides attribute dictionaries, and includes detailed explanations for each taxonomy attribute:

https://github.com/gem/oq-gem-taxonomy.

### Other resources

Additional resources for exploring and working with the taxonomy include:

- [Taxonomy structure](https://tools.openquake.org/taxonomy/structure/attribute/) – Explore the detailed structure and attributes of the taxonomy.

- [Taxonomy graph](https://tools.openquake.org/taxonomy/graph) – Visualize the relationships within the taxonomy.

- [Taxonomy Glossary](https://taxonomy.openquake.org/) – A comprehensive glossary to help you understand the terminology used within the taxonomy.

![Taxonomy_glossary](figures/glossary-lfinf.png)


## Documentation

- [2022]: A Building Classification System for Multi-hazard Risk Assessment (Silva et al. 2022). International Journal for Disaster Risk Science. https://doi.org/10.1007/s13753-022-00400-x
- [2018]: GED4ALL Taxonomy. [Global Exposure Database for Multi-Hazard Risk Analysis-Multi-hazard Exposure Taxonomy](https://www.globalquakemodel.org/gempublications/global-exposure-database-for-multi-hazard-risk-analysis-multi-hazard-exposure-taxonomy). Extension to GED4All Taxonomy for multi-hazard risk assessment. Uses as a reference the GEM Taxonomy v3.0.
- [2013]: [GEM Building Taxonomy v2.0](https://www.globalquakemodel.org/gempublications/gem-building-taxonomy-version-2.0). Initial version of the GEM Building Taxonomy for seismic risk assessment.

## Licensing

- **Code**: Licensed under the [GNU Affero General Public License v3.0](./LICENSE).
- **Data**: Licensed under the [Creative Commons Attribution Share Alike 4.0 International](./DATA_LICENSE).

Please refer to the respective license files for more details.
