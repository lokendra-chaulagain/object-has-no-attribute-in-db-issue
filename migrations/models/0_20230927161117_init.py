from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "table" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS "sale" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "discount_amount" DOUBLE PRECISION NOT NULL  DEFAULT 0,
    "is_draft" BOOL NOT NULL  DEFAULT True,
    "table_id" INT NOT NULL REFERENCES "table" ("id") ON DELETE NO ACTION
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
