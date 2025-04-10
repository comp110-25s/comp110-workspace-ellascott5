"""Examples of set and dictionary syntax."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}
ice_cream["mint"] = 3
ice_cream
{"chocolate": 12, "vanilla": 8, "strawberry": 4, "mint": 3}
ice_cream["strawberry"]
4
print(ice_cream["chocolate"])
12
ice_cream["vanilla"] = 10
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("No orders of mint.")

ice_cream.pop("strawberry")
