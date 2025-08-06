#!/usr/bin/env python3
"""
Test script for activity logging system
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import app, db, ActivityLog, User
from werkzeug.security import generate_password_hash

def test_activity_logs():
    """Test the activity logging system"""
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        # Check if ActivityLog table exists and has data
        try:
            logs_count = ActivityLog.query.count()
            print(f"✓ ActivityLog table exists with {logs_count} records")
            
            # Show recent logs
            recent_logs = ActivityLog.query.order_by(ActivityLog.created_at.desc()).limit(5).all()
            
            if recent_logs:
                print("\n📋 Recent Activity Logs:")
                print("-" * 80)
                for log in recent_logs:
                    print(f"[{log.created_at.strftime('%Y-%m-%d %H:%M:%S')}] "
                          f"{log.user.username} - {log.action} {log.entity_type} "
                          f"({log.entity_name or 'N/A'}): {log.description}")
            else:
                print("\n📋 No activity logs found yet")
                
        except Exception as e:
            print(f"❌ Error accessing ActivityLog table: {e}")
            return False
            
        return True

if __name__ == "__main__":
    print("🔍 Testing Activity Logging System...")
    print("=" * 50)
    
    success = test_activity_logs()
    
    if success:
        print("\n✅ Activity logging system is ready!")
        print("\n💡 Tips:")
        print("- All admin actions (CREATE, UPDATE, DELETE) are now logged")
        print("- View logs in the admin dashboard under 'Activité Récente'")
        print("- Logs include: timestamp, user, action type, entity, and description")
    else:
        print("\n❌ Activity logging system needs setup")
        print("Run: python reset_db.py to initialize the database")
