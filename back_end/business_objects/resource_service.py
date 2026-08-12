from back_end.database.models import Resource, Resource_Trade, Resource_Contact
from back_end.database.database import get_db_context

class Resource_Service:
    def __init__(self):
        pass

    def create_resource(self, name, subcontractor=False):
        with get_db_context() as db:
            new_resource = Resource(
                name = name,
                subcontractor = subcontractor
            )

            db.add(new_resource)
            db.commit()
            id = new_resource.id
            return id
        
    def read_resource(self, resource_id):
        with get_db_context() as db:
            if resource_id:
                resource = db.query(Resource).get(resource_id)
            return resource

    def read_resource_all(self):
        with get_db_context() as db:
            return db.query(Resource)

    def update_resource(self, resource_id, name=None, subcontractor=None):
        with get_db_context() as db:
            if resource_id:
                resource = db.query(Resource).get(resource_id)
                if name:
                    resource.name = name

                if subcontractor:
                    resource.subcontractor = subcontractor

                db.commit()
                return True

    def delete_resource(self, resource_id):
        with get_db_context() as db:
            if resource_id:
                db.delete(resource_id)
                db.commit()

                return True
            else:
                return False


    def create_resource_contact (self, resource_id, name, email=None, phone=None, role=None):
        with get_db_context() as db:
            new_resource_contact = Resource_Contact(
                resource_id = resource_id,
                name = name,
                email = email,
                phone = phone,
                role = role
            )

            db.add(new_resource_contact)
            db.commit()
            id = new_resource_contact.id
            return id
        
    def read_resource_contact(self,contact_id):
        with get_db_context() as db:
            if contact_id:
                resource = db.query(Resource_Contact).get(contact_id)
            return resource
        
    def read_resource_contact_resource(self, resource_id):
        with get_db_context() as db:
            return db.query(Resource_Contact).filter(Resource_Contact.resource_id == resource_id).all()

    def read_resource_contact_all(self,):
        with get_db_context() as db:
            return db.query(Resource_Contact)

    def update_resource_contact (self, resource_contact_id, resource_id=None, name=None, email=None, phone=None, role=None):
        with get_db_context() as db:
            if resource_contact_id:
                resource_contact = db.query(Resource_Contact).get(resource_contact_id)
                if resource_id:
                    resource_contact.resource_id = resource_id
                if name:
                    resource_contact.name = name

                if email:
                    resource_contact.email = email

                if phone:
                    resource_contact.phone = phone

                if role:
                    resource_contact.role = role

                db.commit()
                return True

    def delete_resource_contact(self, resource_contact_id):
        with get_db_context() as db:
            if resource_contact_id:
                db.delete(resource_contact_id)
                db.commit()

                return True
            else:
                return False

    def create_resource_trade(self, trade):
        with get_db_context() as db:
            new_resource_trade = Resource(
                trade = trade,
            )

            db.add(new_resource_trade)
            db.commit()
            id = new_resource_trade.id
            return id

    def read_resource_trade(self, trade_id):
        with get_db_context() as db:
            if trade_id:
                resource = db.query(Resource_Trade).get(trade_id)
            return resource
        
    def read_resource_trade_resource(self, resource_id):
        with get_db_context() as db:
            return db.query(Resource_Trade).filter(Resource_Trade.resource_id == resource_id).all()
        
    def read_resource_trade_all(self,):
        with get_db_context() as db:
            return db.query(Resource_Trade)
        
    def update_resource_trade(self, resource_trade_id, trade):
        with get_db_context() as db:
            if resource_trade_id:
                resource_trade = db.query(Resource_Trade).get(resource_trade_id)
                if trade:
                    resource_trade.trade = trade

                db.commit()
                return True
            else:
                return False

    def delete_resource_trade(self, resource_trade_id):
        with get_db_context() as db:
            if resource_trade_id:
                db.delete(resource_trade_id)
                db.commit
                return True
            
if __name__ == "__main__":
    resource_service = Resource_Service()
    id = resource_service.create_resource("John Smith", False)
    
    print(id)