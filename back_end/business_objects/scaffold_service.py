from back_end.database.models import Scaffold_Request, Scaffold_Elevation, Scaffold_Checklist_Item, Scaffold_Media
from back_end.database.database import get_db_context

class Scaffold_Service:
    def __init__(self):
        pass

    def create_scaffold_request(self, job_id, status, use=None, resource_id=None):
        with get_db_context() as db:
            new_scaffold_request = Scaffold_Request(
                job_id = job_id,
                status = status,
                use = use,
                resource_id = resource_id
            )
            db.add(new_scaffold_request)
            db.commit()
            return new_scaffold_request.id
        

    def read_scaffold(self, scaffold_id):
        with get_db_context() as db:
            scaffold = db.query(Scaffold_Request).get(scaffold_id)
            return scaffold
        
    def read_scaffold_all(self, scaffold_id=None, job_id=None, resource_id=None):
        with get_db_context() as db:
            scaffold_requests = db.query(Scaffold_Request)

            if scaffold_id:
                scaffold_requests = scaffold_requests.filter(scaffold_id)

            if job_id:
                scaffold_requests = scaffold_requests.filter(job_id)

            if resource_id:
                scaffold_requests = scaffold_requests.filter(resource_id)

            return scaffold_requests
        
    def update_scaffold_request(self, scaffold_request_id, job_id=None, use=None, status=None, resource_id=None):
        with get_db_context() as db:
            if scaffold_request_id:
                scaffold = db.query(Scaffold_Request).get(scaffold_request_id)
                if job_id:
                    scaffold.job_id = job_id

                if use:
                    scaffold.use = use

                if status:
                    scaffold.status = status

                if resource_id:
                    scaffold.resource_id = resource_id

                db.commit(scaffold)
                return True
            else:
                return False
        
    def delete_scaffold_request(self, scaffold_request_id):
        with get_db_context() as db:
            scaffold = db.query(Scaffold_Request).get(scaffold_request_id)
            db.delete(scaffold)
            db.commit()
            return True
        
            
    def create_scaffold_elevation(self, scaffold_id, elevation, height, width, chimney, notes=None):
        with get_db_context() as db:
            scaffold = Scaffold_Elevation(
                scaffold_id = scaffold_id,
                elevation = elevation,
                height = height,
                width = width,
                chimney = chimney,
                notes = notes
            )

            db.add(scaffold)
            db.commit()

            return scaffold.id

    def read_scaffold_elevation(self, elevation_id):
        with get_db_context() as db:
            elevation = db.query(Scaffold_Elevation).get(elevation_id)

            return elevation

    def update_scaffold_elevation(self, elevation_id, scaffold_id=None, elevation=None, height=None, width=None, chimney=None, notes=None):
        with get_db_context() as db:
            if elevation_id:
                elevation_instance = db.query.get(elevation_id)
                if scaffold_id:
                    elevation_instance.scaffold_id = scaffold_id
                if elevation:
                    elevation_instance.elevation = elevation
                if height:
                    elevation_instance.height = height
                if width:
                    elevation_instance.width = width
                if chimney:
                    elevation_instance.chimney = chimney
                if notes:
                    elevation_instance.notes = notes
                
                db.commit()
                return True
            else:
                return False

    def delete_scaffold_elevation(self, elevation_id):
        with get_db_context() as db:
            if elevation_id:
                elevation = db.query(Scaffold_Elevation).get(elevation_id)
                db.delete(elevation)
                db.commit()
                return True
            else:
                return False


    def create_scaffold_checklist_item(self, check_item):
        with get_db_context() as db:
            scaffold_checklist_item = Scaffold_Checklist_Item(
                check_item = check_item
            )

            db.add(scaffold_checklist_item)
            db.commit()
            
            return scaffold_checklist_item.id
        
    def read_scaffold_checklist_item(self, item_id):
        with get_db_context() as db:
            item = db.query(Scaffold_Checklist_Item).get(item_id)

            return item

    def update_scaffold_checklist_item(self, checklist_id, check_item):
        with get_db_context() as db:
            checklist_item = db.query(Scaffold_Checklist_Item).get(checklist_id)
            if check_item:
                checklist_item.check_item = check_item
                db.commit()
                return True
            else:
                return False


    def delete_scaffold_checklist_item(self, checklist_id):
        with get_db_context() as db:
            if checklist_id:
                checklist_item = db.query(Scaffold_Checklist_Item).get(checklist_id)
                db.delete(checklist_item)
                db.commit()
                return True
            else:
                return False


    def create_scaffold_media(self, scaffold_id, document_name, document, scaffold_media_type, scaffold_checklist_item_id=None):
        with get_db_context() as db:
            scaffold_media = Scaffold_Media(
                scaffold_id = scaffold_id,
                document_name = document_name,
                document = document,
                scaffold_checklist_item_id = scaffold_checklist_item_id,
                scaffold_media_type = scaffold_media_type
            )

            db.add(scaffold_media)
            db.commit()

            return scaffold_media.id
            
    def read_scaffold_media(self, media_id):
        with get_db_context() as db:
            media = db.query(Scaffold_Media).get(media_id)

            return media

    def update_scaffold_media(self, media_id, scaffold_id=None, document_name=None, document=None, scaffold_checklist_item_id=None, scaffold_media_type=None):
        with get_db_context() as db:
            if media_id:
                media = db.query(Scaffold_Media).get(media_id)
                if scaffold_id:
                    media.scaffold_id = scaffold_id

                if document_name:
                    media.document_name = document_name

                if document:
                    media.document = document

                if scaffold_checklist_item_id:
                    media.scaffold_checklist_item_id = scaffold_checklist_item_id

                if scaffold_media_type:
                    media.scaffold_media_type = scaffold_media_type

                db.commit()
                return True
            else:
                return False


    def delete_scaffold_media(self, media_id):
        with get_db_context() as db:
            if media_id:
                media = db.query(Scaffold_Media).get(media_id)
                db.delete(media)
                db.commit()
                return True
            
if __name__ == "__main__":
    scaffold_service = Scaffold_Service()
    id = scaffold_service.create_scaffold_request("f7b2a62f-0722-4db7-93ce-102b75d2ef0a", "REQUESTED", "Inspection", "e0d0902b-08b6-424e-8942-7bcfe0a66a3e")
    print(id)