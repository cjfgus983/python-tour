# Tourist Data Analysis Project

## Overview

This project analyzes various aspects of tourism data in Korea, including the number of foreign visitors, their purpose of visit, satisfaction levels, and the most visited cities and areas. The project uses several datasets to generate visualizations and insights.

## Requirements

### Necessary Downloads or Installations

1. **Python Environment**: Ensure you have Python 3.8 or later installed.
2. **Libraries**: Install the necessary Python libraries using the following command:

   ```sh
   pip install -r requirements.txt
   ```

   The `requirements.txt` should include:

   ```
   glob2
   matplotlib
   seaborn
   pandas
   folium
   googlemaps
   scikit-learn
   yellowbrick
   numpy
   ```

   if you can't download Library at terminal, use Anaconda Navigator

3. **Fonts**: The project uses the GULIM font to display Korean characters in graphs. If the GULIM font is not installed on your system, download and install it. Alternatively, you can modify the code to use a different font that supports Korean characters.

### Data

- **Datasets**: The following datasets are used in the project:
  - `데이터셋/방한관광객.csv`
  - `데이터셋/만족도데이터.csv`
  - `데이터셋/권역방문데이터.csv`
  - `데이터셋/서울전체.csv`
  - `데이터셋/강남구.csv`
  - `데이터셋/중구.csv`
  - `데이터셋/송파구.csv`

If the data is not publicly available, you can download it from
https://mdis.kostat.go.kr/mypage/extract/viewMyExtractListNew.do?curMenuNo=UI_POR_P9030#data_down

https://datalab.visitkorea.or.kr/datalab/portal/nat/getForTourForm.do#

https://datalab.visitkorea.or.kr/datalab/portal/loc/getAreaDataForm.do

Ensure the datasets are placed in a folder named `데이터셋` within your project directory.

## Description of Files

- **main.py**: The main script that executes all data analysis and visualization functions.
- **clustering.py**: Contains the `clustering_path` function to perform clustering on the tourist area data and visualize it on Google Maps.
- **find_main_area.py**: Contains the `find_area` function to analyze and visualize the distribution of tourist spots in different districts.
- **city_visit.py**: Contains the `city_visit_graph` function to visualize the cities visited by foreign tourists.
- **satisfaction.py**: Contains the `satisfaction_graph` function to visualize the satisfaction levels of tourists across various aspects.
- **visit_korea_count.py**: Contains the `visit_korea_count_func` function to analyze and visualize the number of foreign visitors.
- **purpose_visit.py**: Contains the `purpose_visit_korea` function to analyze and visualize the purpose of visits by foreign tourists.
- **test.py**: A test script to verify the functionality of each module and function.

## Setup and Instructions

### Step-by-Step Instructions

1. **Clone the Repository**: Clone the project repository to your local machine.

   ```sh
   git clone <repository_link>
   cd <repository_directory>
   ```

2. **Install Dependencies**: Install the required Python libraries.

   ```sh
   pip install -r requirements.txt
   ```

3. **Download Datasets**: Ensure all required datasets are downloaded and placed in the `데이터셋` directory. If provided through a link, download and extract them as instructed.

4. **Font Installation**:

   - If the GULIM font is not installed on your system, download and install it from a reliable source.
   - Alternatively, modify the following line in `main.py` to use a different font that supports Korean characters:
     ```python
     plt.rc('font', family='GULIM')
     ```
     Replace `'GULIM'` with another font name available on your system.

5. **Run the Main Script**: Execute the `main.py` script to perform all analyses and generate visualizations.

   ```sh
   python main.py
   ```

6. **Run the Test Script**: Execute the `test.py` script to verify that all functions are working correctly.
   ```sh
   python test.py
   ```

### Output Files

After running `main.py`, the following output files will be generated:

- **PNG Files**: These files contain various graphs and visualizations based on the analysis.
  - For example, satisfaction graphs, clustering elbow method plots, and other visual data representations.
- **HTML Files**: These files display the clustering results on Google Maps.
  - Each HTML file opens in a web browser and shows the clustered locations with markers.

### Detailed Function Descriptions

- **visit_korea_count_func(file_path)**: Reads the dataset containing the number of foreign visitors and generates a relevant visualization.
- **purpose_visit_korea()**: Analyzes and visualizes the purpose of visits by foreign tourists.
- **satisfaction_graph(file_path, column_type)**: Generates satisfaction graphs for various aspects such as overall satisfaction, public transportation, accommodation, food, etc.
- **city_visit_graph(file_path)**: Visualizes the cities most visited by foreign tourists.
- **find_area(file_path)**: Analyzes and visualizes the distribution of tourist spots in different districts of Seoul.
- **clustering_path(file_path, save_file_name, k_count)**: Performs clustering on tourist area data and visualizes it on Google Maps. It helps identify where to place tourist information centers.

## Additional Information

- Ensure your working directory is set to the project root where `main.py` is located.
- The datasets must be in the correct format as expected by the scripts.

With these instructions, you should be able to set up and run the project to reproduce the results. If you encounter any issues, please refer to the error messages or check the file paths and dataset contents.
