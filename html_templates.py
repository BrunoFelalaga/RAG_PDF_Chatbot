my_css = '''
<style>
.custom-chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
}
.custom-chat-message.user {
    background-color: #2b313e;
}
.custom-chat-message.bot {
    background-color: #475063;
}
.custom-chat-message .custom-avatar {
    width: 20%;
}
.custom-chat-message .custom-avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.custom-chat-message .custom-message {
    width: 80%;
    padding: 0 1.5rem;
    color: #fff;
}
</style>
'''

my_bot_template = '''
<div class="custom-chat-message bot">
    <div class="custom-avatar">
        <img src="chat_bot_avatar.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="custom-message">{{MSG}}</div>
</div>
'''

my_user_template = '''
<div class="custom-chat-message user">
    <div class="custom-avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="custom-message">{{MSG}}</div>
</div>
'''
