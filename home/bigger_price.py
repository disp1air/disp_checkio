def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # student_tuples = [
    #     ('john', 'A', 15),
    #     ('jane', 'B', 12),
    #     ('dave', 'B', 10),
    # ]
    # sorted(student_tuples, key=lambda student: student[2])   # сортируем по возрасту
    # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
    return sorted(data, key=lambda item: item['price'], reverse=True)[:limit]


if __name__ == '__main__':
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ]

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}]
