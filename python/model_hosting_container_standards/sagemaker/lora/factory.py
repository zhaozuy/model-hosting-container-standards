from typing import Callable

from ...common.transforms.base_factory import create_transform_decorator
from .transforms import resolve_lora_transform


def create_lora_transform_decorator(handler_type: str) -> Callable:
    return create_transform_decorator(handler_type, resolve_lora_transform)
