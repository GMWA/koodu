from flask_restful import reqparse
from werkzeug.exceptions import default_exceptions

get_parser =  reqparse.RequestParser()
get_parser.add_argument(
    "name",
    type=str,
    help="name is required",
    location=("json", "values")
)
get_parser.add_argument(
    "description",
    type=str,
    help="description is required",
    location=("json", "values")
)


post_parser =  reqparse.RequestParser()
post_parser.add_argument(
    "name",
    type=str,
    help="name is required",
    location=("json", "values")
)
post_parser.add_argument(
    "description",
    type=str,
    help="description is required",
    location=("json", "values")
)


update_parser =  reqparse.RequestParser()
update_parser =  reqparse.RequestParser()
update_parser.add_argument(
    "id",
    type=int,
    help="id is required",
    location=("json", "values")
)
update_parser.add_argument(
    "name",
    type=str,
    help="name is required",
    location=("json", "values")
)
update_parser.add_argument(
    "description",
    type=str,
    help="description is required",
    location=("json", "values")
)


delete_parser =  reqparse.RequestParser()
delete_parser.add_argument(
    "int",
    type=int,
    help="id is required",
    location=("json", "values")
)