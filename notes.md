## Topics
1. [Path Parameters](#path-parameters)
2. [Query Parameters](#query-parameters)
3. [Post Request Method](#post-request-method)
4. [Put Request Method](#put-request-method)
5. [Delete Request Method](#delete-request-method)
6. [Usage of Pydantic](#usage-of-pydantic)


## Path Parameters
- Path parameters are request parameters that have been attached to the url
- They are usually defined as a way to find information based on location
```python
    @app.get("/blog/{id}")
    def get_blog(id: int):
         return {"id": id}
```
- Here Id is the path parameter (dynamic params)
- Important to place the static api before than this dynamic api's

## Query Parameters
- Query parameters are request parameters that have been attached to the url after a ?
- Query parameters have name = value pairs
```bash
    http://127.0.0.1:8000/blog?limit=10&published=True 
```
```python
    @app.get("/blog")
    def get_blog(limit: int = 10, published: bool = True):
        return {"data": f"{limit} published {published}"}
```

## Post Request Method
- Post request Method are used to create data
```python
    from fastapi import Body
    @app.post("/blog")
    def create_blog(request: Body()):
        return Blog.append(request)
```

## Put Request Method
- Put request Method are used to update data
```python
    from fastapi import Body
    @app.put("/blog/{id}")
    def update_blog(id: int, request: Body()):
        Blog[id] = request
        return {"data": f"Blog with id {id} has been updated"}
```

## Delete Request Method
- Delete request Method are used to delete data
```python
    @app.delete("/blog/{id}")
    def delete_blog(id: int):
        for idx in range(len(Blog)):
            if Blog[idx]["id"] == id:
                Blog.pop(idx)
                break
        return {"data": f"Blog with id {id} has been deleted"}
```

## Usage of Pydantic
- Pydantic is a data validation library
- It is used to validate the data before processing
