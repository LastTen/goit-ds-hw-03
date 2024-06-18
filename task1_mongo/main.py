from connect_mongo import db


# def add_to_db(name: str, age: int, features: list = []):
#     """add a new document to the database"""
#     result_one = db.cats.insert_one(
#         {
#             "name": name,
#             "age": age,
#             "features": features,
#         }
#     )

#     print(result_one.inserted_id)


def get_all_data():
    """get all documents from the database"""
    count = db.cats.count_documents({})
    if count == 0:
        print(f"Database has no documents")
    else:
        result = db.cats.find()
        for el in result:
            print(el)


def get_if_name(name: str = None):
    """get a document by name"""
    if name is None:
        print(f"Enter name")
    else:
        count = db.cats.count_documents({"name": name})
        if count == 0:
            print(f"{name} not found")
        else:
            result = db.cats.find({"name": name})
            for el in result:
                print(el)


def update_age_by_name(name: str = None, age: int = None):
    """update age by name"""
    if name is None or age is None:
        print(f"Enter name and age")
    else:
        result = db.cats.update_one(
            {"name": name}, {"$set": {"age": age}}, upsert=False
        )

        if result.modified_count > 0:
            print(f"Age for {name} has been updated")
        else:
            print(f"{name} not found")


def add_new_features_to_db(name: str = None, feature: str = None):
    """Add new features for name"""
    if name is None or feature is None:
        print(f"Enter name and feature")
    else:
        result = db.cats.update_one(
            {"name": name}, {"$addToSet": {"features": feature}}
        )

        if result.modified_count > 0:
            print(f"Feature '{feature}' add to '{name}'.")
        else:
            print(f"{name} not found")


def delete_by_name(name: str = None):
    """delete a document by name"""
    if name is None:
        print(f"Enter name")
    else:
        result = db.cats.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"{name} has been deleted")
        else:
            print(f"{name} not found")


def delete_all():
    """delete all documents from the database"""
    result = db.cats.delete_many({})
    print(f"{result.deleted_count} documents has been deleted")


if __name__ == "__main__":
    # add_to_db("test", 3, ["foo", "bar", "baz"])
    get_all_data()
    get_if_name("test")
    update_age_by_name("test", 4)
    add_new_features_to_db("test", "dii")
    delete_by_name("test")
    delete_all()

    # add_to_db("test2", 3, ["foo", "bar", "baz"])
    # get_all_data()
    # get_if_name()
    # update_age_by_name()
    # add_new_features_to_db()
    # delete_by_name()
    # delete_all()
