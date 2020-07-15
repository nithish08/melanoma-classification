# Can we detect melanoma using lesion images

> https://www.kaggle.com/c/siim-isic-melanoma-classification/overview/description


## Data Exploration

1. Highly imbalanced dataset.

![](images/imbalanced.jpg)

2. Train - Test size

![](images/train-test-size.jpg)




## Baseline

Tabular features in the dataset.

|    | image_name   | patient_id   | sex    |   age_approx | anatom_site_general_challenge   | diagnosis   | benign_malignant   |   target |
|---:|:-------------|:-------------|:-------|-------------:|:--------------------------------|:------------|:-------------------|---------:|
|  0 | ISIC_2637011 | IP_7279968   | male   |           45 | head/neck                       | unknown     | benign             |        0 |
|  1 | ISIC_0015719 | IP_3075186   | female |           45 | upper extremity                 | unknown     | benign             |        0 |
|  2 | ISIC_0052212 | IP_2842074   | female |           50 | lower extremity                 | nevus       | benign             |        0 |
|  3 | ISIC_0068279 | IP_6890425   | female |           45 | head/neck                       | unknown     | benign             |        0 |
|  4 | ISIC_0074268 | IP_8723313   | female |           55 | upper extremity                 | unknown     | benign             |        0 |

### 5-fold-cv with tabular features:
![](images/tab-features-5-fold-cv.jpg)







