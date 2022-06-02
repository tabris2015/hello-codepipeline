def create_users_table(dynamodb, table_name):
    # Table defination
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {"AttributeName": "username", "KeyType": "HASH"},  # Partition key
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "username",
                # AttributeType defines the data type. "S" is string type and "N" is number type
                "AttributeType": "S",
            },
        ],
        ProvisionedThroughput={
            # ReadCapacityUnits set to 10 strongly consistent reads per second
            "ReadCapacityUnits": 10,
            "WriteCapacityUnits": 10,  # WriteCapacityUnits set to 10 writes per second
        },
    )
    return table


if __name__ == "__main__":
    device_table = create_users_table()
    # Print table status
    print("Status:", device_table.table_status)
