from prefect import flow, task
from ..etl import process_csv

@task
def read_and_validate(path: str):
    print("Prefect task: read_and_validate", path)
    process_csv(path)
    return True

@flow
def bank_pipeline(path: str):
    print("Startar Prefect flow för", path)
    ok = read_and_validate(path)
    print("Flow klart:", ok)

if __name__ == '__main__':
    bank_pipeline('data/test_transactions.csv')
