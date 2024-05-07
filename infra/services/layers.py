from aws_cdk import aws_lambda as _lambda
from lambda_forge import Path


class Layers:
    def __init__(self, scope) -> None:

        # self.layer = _lambda.LayerVersion.from_layer_version_arn(
        #     scope,
        #     id="Layer",
        #     layer_version_arn="",
        # )
        ...

        self.sm_utils_layer = _lambda.LayerVersion(
            scope,
            id="SmUtilsLayer",
            code=_lambda.Code.from_asset(Path.layer("layers/sm_utils")),
            compatible_runtimes=[_lambda.Runtime.PYTHON_3_9],
            description="",
        )
