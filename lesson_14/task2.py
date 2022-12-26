class Snow:
    def __init__(self, snowflake_count: int):
        self.snowflake_count = snowflake_count

    def __str__(self):
        return f"snowflake = {self.snowflake_count}"

    def add(self, n):
        self.snowflake_count += n

    def sub(self, n):
        self.snowflake_count -= n

    def mul(self, n):
        self.snowflake_count *= n

    def div(self, n):
        self.snowflake_count /= n

    def makeSnow(self, snowflake_count_in_row):
        row_count = self.snowflake_count // snowflake_count_in_row
        rest_count = self.snowflake_count % snowflake_count_in_row
        for _ in range(row_count):
            print("*" * snowflake_count_in_row)
        print("*" * rest_count)

# snowflake1 = Snow(99)
# snowflake1.add(10)
# snowflake1.makeSnow(10)

