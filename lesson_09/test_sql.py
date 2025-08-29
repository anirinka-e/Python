from Sql import Sql

sql = Sql("postgresql://postgres:123@localhost:5432/QA")


def test_select():
    result = sql.select()
    print(result)

    assert len(result) == 15


def test_insert():
    result_select = sql.select()
    subject_id = result_select[-1]["subject_id"] + 1
    sql.insert(subject_id, 'Game theory')
    result_insert = sql.select()

    sql.delete(subject_id)

    assert result_insert[-1]["subject_id"] == 16
    assert result_insert[-1]["subject_title"] == 'Game theory'


def test_update():
    result_select = sql.select()
    subject_id = result_select[-1]["subject_id"] + 1
    sql.insert(subject_id, 'Game theory')

    sql.update(subject_id, 'Other')
    result_update = sql.select()

    sql.delete(subject_id)

    assert result_update[-1]["subject_id"] == 16
    assert result_update[-1]["subject_title"] == 'Other'


def test_delete():
    result_select = sql.select()
    subject_id = result_select[-1]["subject_id"] + 1
    sql.insert(subject_id, 'Game theory')

    sql.delete(subject_id)
    result_delete = sql.select()

    assert result_delete[-1]["subject_id"] == subject_id - 1
