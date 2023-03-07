import os
from pathlib import Path
import random
import pandas as pd

random.seed(41)


def generate_random_solution(f):
    bbox = [50, 50, 100, 100]
    conf = random.random()
    label = random.randint(0, 1)
    image_id = f.name[:-len(f.suffix)]

    result = {
        'image_id': image_id,
        'xmin': bbox[0],
        'ymin': bbox[1],
        'xmax': bbox[2],
        'ymax': bbox[3],
        'label': label,
        'score': round(conf, 4)
    }
    return result


def create_simple_solution():
    root_path = os.environ['DATA_ROOT_PATH']

    results = []
    for f in Path(root_path).glob('*'):
        if random.random() > 0.7:
            for _ in range(3):
                results.append(generate_random_solution(f))
        else:
            results.append(generate_random_solution(f))

    test_df = pd.DataFrame(results, columns=['image_id', 'xmin', 'ymin', 'xmax', 'ymax', 'label', 'score'])
    test_df.to_csv('submission.csv', index=False)


create_simple_solution()
