@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        example= 123
    ) #mayor a cero
):
    return {person_id: "It exists!"}