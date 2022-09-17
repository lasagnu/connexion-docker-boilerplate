from attrs import define, field

@define
class DefaultMessage:
    message: str

    def serialize(self):
        return {'message': self.message}