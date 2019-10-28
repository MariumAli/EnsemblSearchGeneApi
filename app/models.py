from app import db


class GeneAutoComplete(db.Model):
    """Data model for gene autocomplete table."""
    __tablename__ = 'gene_autocomplete'

    species = db.Column(db.String(255), nullable=True, primary_key=True)
    stable_id = db.Column(db.String(128), nullable=False, default='', primary_key=True)
    display_label = db.Column(db.String(128), nullable=True, primary_key=True)
    location = db.Column(db.String(60), nullable=True)
    db = db.Column(db.String(32), nullable=False, default='core')
    # db.PrimaryKeyConstraint('species', 'display_label', name='i')
    # db.PrimaryKeyConstraint('species', 'stable_id', name='i2')
    # db.PrimaryKeyConstraint('species', 'display_label', 'stable_id', name='i3')

    def __init__(self, species, stable_id, display_label, location, db):
        self.species = species
        self.stable_id = stable_id
        self.display_label = display_label
        self.location = location
        self.db = db


    def __repr__(self):
        return '<Gene {}>'.format(self.stable_id)
