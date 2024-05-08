from django.db import models
from django.utils import timezone

from django.conf import settings

class ConversationParticipant(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	# This will hold the conversation's symmetric key, encrypted with the user's public asymetric key.
	encrypted_key = models.BinaryField(max_length=50, blank=True) # ??? length TODO (this field isn't used at all yet)

class Conversation(models.Model):
	participants = models.ManyToManyField(to=ConversationParticipant)
	start_date = models.DateTimeField("date of first message", default=timezone.now)

	@classmethod
	def available_to_user(cls, conversation_id, user_id):
		return Conversation.objects.filter(id=conversation_id, participants__user__id=user_id).count() == 1

	def get_last_message(self):
		return Message.objects.filter(conversation_id=self.id).order_by('-date').first()

class Message(models.Model):
	conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
	text = models.BinaryField(max_length=2000, blank=False)
	date = models.DateTimeField(default=timezone.now)

	class Meta:
		indexes = [
			models.Index(fields=['date'])
		]

	def json_serializable(self):
		return {
			'message': self.text.decode(),
			'username': self.user.get_full_name(),
			'time': str(self.date),
		}
