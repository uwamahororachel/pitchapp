from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,RadioField
from wtforms.validators import Required
class PitchForm(FlaskForm):
   title = StringField('Pitch Title',validators=[Required()])
   description = TextAreaField('Pitch Description', validators=[Required()]) 
   category = RadioField('Label', choices=[ ('Interview','Interview'), ('Business','Business'),('Promotion','Promotion'),('Product','Product')],validators=[Required()])
   submit = SubmitField('Submit')


class CommentForm(FlaskForm):
	description = TextAreaField('comment here',validators=[Required()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
	submit = SubmitField()
class UpdateProfile(FlaskForm):
   bio = TextAreaField('Tell us more about you',validators = [Required()])
   submit = SubmitField('Submit')


