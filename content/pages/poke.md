title: Poke Me!
description: Send Pratyush a message
slug: poke


<form action="http://getsimpleform.com/messages?form_api_token=c490e670498433a14f0b9036a42cc60f" method="post">
  <!-- the redirect_to is optional, the form will redirect to the referrer on submission -->
  <input type='hidden' name='redirect_to' value='http://fully-faltoo.com' />
  <p>Hi Pratyush,</p>
  <textarea name='message' placeholder='Message...' rows='5' cols='50'></textarea><br>
  <input type='text' name='from' placeholder='Email' />
  <input type='submit' value='Send' />
</form>