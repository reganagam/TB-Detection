# TB-Detection
## Biomedical Project by Regan Agam
### Penjelasan Dataset
Data sekunder yang digunakan pada penelitian ini diambil dari RSUP dr. Rivai Abdullah yang beralamat di Jl. Sungai Kundur, Sungai Kedukan, Kec. Banyuasin I, Kab. Banyuasin, Sumatera Selatan. Pengambilan data berupa citra chest X-ray penyakit tuberkulosis (TB), normal, dan covid-19 dengan jumlah 141 data normal, 149 data TB, dan 279 data covid-19, dimana data tersebut berasal dari warga Banyuasin dan sekitarnya. Selain data dari RSUP dr. Rivai Abdullah, data lainnya didapatkan dari Kaggle. Data yang didapatkan dari Kaggle untuk data tuberkulosis dan normal merupakan data gabungan yang berasal dari BELARUS TB portal program dataset, NLM, RSNA dengan jumlah 3500 data normal dan 700 data TB, dan juga dataset tuberkulosis dari Shenzen (China) dengan jumlah 662. Kemudian, dataset covid-19 yang juga didapatkan dari Kaggle merupakan data gabungan dari padchest dataset, Germany medical school, SIRM, dan GitHub dengan jumlah 3500 data covid-19.
Terdapat 3 jenis dataset yang saya buat untuk melihat apakah perbedaan sumber berpengaruh terhadap hasil yang didapat dari hasil penyeimbangan jumlah data secara keseluruhan dan sesuai dengan kebutuhan, datasetnya terdiri dari:
- Dataset Kaggle = Dataset yang bersumber dari internet (kaggle).
- Dataset RSUP = Dataset yang bersumber dari RSUP dr. Rivai Abdullah.
- Dataset Gabungan = Dataset yang bersumber dari gabungan dataset Kaggle dan RSUP.
Adapun untuk dataset uji, terbagi menjadi 3 jenis dataset yang terbagi menjadi:
- Testing Kaggle = Dataset untuk pengujian yang bersumber dari internet (kaggle).
- Testing RSUP = Dataset untuk pengujian yang bersumber dari RSUP dr. Rivai Abdullah.
- Data uji baru = Dataset baru untuk pengujian akhir UI yang bersumber dari RSUP dr. Rivai Abdullah.
### Penjelasan tiap komponen folder & file
- Confusion Matrix = Folder yang berisi jupyter file untuk pengujian model yang berupa confusion matrix. File yang memiliki kode K artinya pengujian menggunakan dataset Testing Kaggle, sedangkan kode R artinya pengujian menggunakan dataset Testing RSUP.
- Resize.py = Python file untuk mengubah seluruh gambar dataset dalam satu folder sehingga memiliki ukuran yang sama semua sesuai yang diinginkan.
- convert_to_greyscale.py = python file untuk mengubah beberapa gambar dalam satu folder menjadi berwarna abu-abu atau warna asli chest x-ray (jika terdapat data yang memiliki warna selain abu-abu untuk meminimalkan bias).
- Script - kaggle.ipynb = Jupyter file untuk melakukan proses training data menggunakan Dataset Kaggle.
- Script - rsup.ipynb = Jupyter file untuk melakukan proses training data menggunakan Dataset RSUP.
- Script - gabungan.ipynb = Jupyter file untuk melakukan proses training data menggunakan Dataset Gabungan.
- Local Deploy.py = Python file untuk melakukan deployment model ke dalam user interface menggunakan library Gradio dengan local hosting.
### Sumber Dataset
- Private dataset dari RSUP dr. Rivai Abdullah yang beralamat di Jl. Sungai Kundur, Sungai Kedukan, Kec. Banyuasin I, Kab. Banyuasin, Sumatera Selatan.
- Kaggle TB 1 = https://www.kaggle.com/datasets/tawsifurrahman/tuberculosis-tb-chest-xray-dataset
- Kaggle TB 2 = https://www.kaggle.com/datasets/raddar/tuberculosis-chest-xrays-shenzhen
- Kaggle Covid = https://www.kaggle.com/datasets/anasmohammedtahir/covidqu
### Python Version dan Library Version yang digunakan pada saat penelitian
- Python 3.9
- Gradio 3.12.0
- Tensorflow 2.11.0
- Tensorflow-gpu 2.11.0
- Keras 2.11.0
- Keras-preprocessing 1.1.2
- Numpy 1.23.5
- Matplotlib 3.7.1
