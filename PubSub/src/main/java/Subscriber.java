import java.util.ArrayList;
import java.util.List;

public abstract class Subscriber {
   /* 1. Add Subscriber to a topic
    2. Unsubscribe from a topic
    3. Store Messages received by a subscriber
    4. get messages for subscriber of topic*/
   public String name;

   public Subscriber(String name){
       this.name = name;
   }

   List<Message> subscriberMessages = new ArrayList<Message>();

   public void setSubscriberMessages(List<Message> subscriberMessages){
       this.subscriberMessages = subscriberMessages;
   }
   public List<Message> getSubscriberMessages(){
       return subscriberMessages;
   }

   public abstract void addSubscriber(String topic, PubSubService pubSubService);
   public abstract void unSubscribe(String topic, PubSubService pubSubService);
   public abstract void getMessagesForSubscriberOfTopic(String topic, PubSubService pubSubService);

   public void printMessages(){
       for(Message message: subscriberMessages){
           System.out.println("Message Topic: " + message.getTopic() + " : " + message.getPayload());
       }
   }

   public void receive(Message message) {
       subscriberMessages.add(message);
       this.setSubscriberMessages(subscriberMessages);
       System.out.println(this.name + ":"+"Message Topic: " + message.getTopic() + " : " + message.getPayload());
   }

}
