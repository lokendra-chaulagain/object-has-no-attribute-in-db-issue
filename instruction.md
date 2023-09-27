# How To Run
# 1. aerich init -t config.Database.TORTOISE_ORM  
# 2. aerich init-db      (first time only)
# 3. aerich migrate    (amke script)
# 4. aerich upgrade    (apply script on db)
# 4. uvicorn main:app --host localhost --port 8000 --reload   (to run)




// Optional
pip freeze > requirements.txt    to generate requirement file