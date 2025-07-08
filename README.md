# Bacterial Protective Antigens Database (BPAdb)

This repository contains a standalone SQLite database (`antigens.db`) which stores information about experimentally validated antigens and immunogenic proteins of WHO prioritized antimicrobial resistant pathogens.

Web version of the database is available at: https://mgbio.tech/bpadb/.

## Usage
- **Prerequisites**: Install SQLite or a compatible client (e.g., DB Browser for SQLite).
- **Accessing the Database**: Use an SQLite client to open `antigens.db`. Example query:
  ```sql
  SELECT * FROM antigens WHERE organism_studied = 'Staphylococcus aureus';


## Copyright
© 2025 MGBioTech. All rights reserved.
The Bacterial Protective Antigens Database (BPAdb) is owned by MGBIO (https://mgbio.tech) and is licensed under the MIT License. It is freely available for research and academic purposes with citation required. Any use for commercial purposes requires prior permission from MGBIO. For inquiries, please contact MGBIO.

## Citation
The Bacterial Protective Antigens Database (BPAdb) is a work in progress developed by MGBIO. A formal publication is forthcoming. Until the paper is published, please cite the database as follows:

MGBioTech. (2025). Bacterial Protective Antigens Database (BPAdb). GitHub Repository. Available at: https://github.com/samavinasir96/BPAdb.git.

Please check back for updates on the publication status or contact MGBio for further information.
