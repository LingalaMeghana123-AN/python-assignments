from pymongo import MongoClient

# Connect to DB
client = MongoClient("mongodb://localhost:27017/")
db = client["studentSkillDB"]

students = db["students"]

# CREATE
def add_student():
    student = {
        "studentName": "Priya",
        "skills": ["DSA", "Java"],
        "level": "Intermediate",
        "practiceHistory": [
            {"date": "2026-03-23", "hours": 2},
            {"date": "2026-03-23", "hours": 3}
        ]
    }
    students.insert_one(student)
    print("✅ Student Added")

# READ
def find_dsa_students():
    print("\n📖 Students with DSA skill:")
    for s in students.find({"skills": "DSA"}):
        print(s)

# UPDATE
def add_skill():
    students.update_one(
        {"studentName": "Priya"},
        {"$addToSet": {"skills": "MongoDB"}}
    )
    print("✏️ Skill Added")

# DELETE
def delete_inactive():
    students.delete_many({"practiceHistory": {"$size": 0}})
    print("❌ Inactive Students Deleted")

# AGGREGATION
def total_hours():
    print("\n📊 Total Hours:")
    pipeline = [
        {"$unwind": "$practiceHistory"},
        {
            "$group": {
                "_id": "$studentName",
                "totalHours": {"$sum": "$practiceHistory.hours"}
            }
        }
    ]
    for r in students.aggregate(pipeline):
        print(r)

def top_student():
    print("\n🏆 Top Student:")
    pipeline = [
        {"$unwind": "$practiceHistory"},
        {
            "$group": {
                "_id": "$studentName",
                "totalHours": {"$sum": "$practiceHistory.hours"}
            }
        },
        {"$sort": {"totalHours": -1}},
        {"$limit": 1}
    ]
    for r in students.aggregate(pipeline):
        print(r)

def daily_summary():
    print("\n📅 Daily Summary:")
    pipeline = [
        {"$unwind": "$practiceHistory"},
        {
            "$group": {
                "_id": "$practiceHistory.date",
                "totalHours": {"$sum": "$practiceHistory.hours"}
            }
        }
    ]
    for r in students.aggregate(pipeline):
        print(r)

# INDEX
def create_indexes():
    students.create_index("studentName")
    students.create_index("skills")
    print("⚡ Indexes Created")

# RUN ALL
def run():
    add_student()
    find_dsa_students()
    add_skill()
    total_hours()
    top_student()
    daily_summary()
    create_indexes()
    delete_inactive()

run()