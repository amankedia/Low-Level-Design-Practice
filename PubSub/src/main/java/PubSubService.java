import java.util.*;

public class PubSubService {

    Map<String, Set<Subscriber>> subscriberTopicMap = new HashMap<String, Set<Subscriber>>();

    Queue<Message> messageQueue = new LinkedList<Message>();

    public void addMessageToQueue(Message message){
        messageQueue.add(message);
    }

    public void addSubscriber(String topic, Subscriber subscriber){
        if(subscriberTopicMap.containsKey(topic)){
            Set<Subscriber> subscribers = subscriberTopicMap.get(topic);
            subscribers.add(subscriber);
            subscriberTopicMap.put(topic, subscribers);
        } else{
            Set<Subscriber> subscribers = new HashSet<Subscriber>();
            subscribers.add(subscriber);
            subscriberTopicMap.put(topic, subscribers);
        }
    }

    public void removeSubscribers(String topic, Subscriber subscriber){
        if(subscriberTopicMap.containsKey(topic)){
            Set<Subscriber> subscribers = subscriberTopicMap.get(topic);
            subscribers.remove(subscriber);
            subscriberTopicMap.put(topic, subscribers);
        }
    }

    public void broadcast(){
        if(messageQueue.isEmpty()){
            System.out.println("No messages from publishers to display");
        } else{
            while(!messageQueue.isEmpty()){

                Message message = messageQueue.remove();
                String topic = message.getTopic();

                Set<Subscriber> subscribersOfTopic = subscriberTopicMap.get(topic);

                for(Subscriber sub : subscribersOfTopic){
//                    List<Message> subscriberMessages = sub.getSubscriberMessages();
//                    subscriberMessages.add(message);
//                    sub.setSubscriberMessages(subscriberMessages);
                    sub.receive(message);
                }

            }
        }
    }

    public void getMessagesForSubscriberOfTopic(String topic, Subscriber subscriber){
        if(messageQueue.isEmpty()){
            System.out.println("Message queue is empty");
        } else {
            while (!messageQueue.isEmpty()){
                Message message = messageQueue.remove();
                String topicOfMessage = message.getTopic();
                if(topicOfMessage.equalsIgnoreCase(topic)){

                    Set<Subscriber> subscribersOfTopic = subscriberTopicMap.get(topic);

                    for(Subscriber sub : subscribersOfTopic){
                        if(sub.equals(subscriber)){
                            List<Message> subscriberMessages = sub.getSubscriberMessages();
                            subscriberMessages.add(message);
                            sub.setSubscriberMessages(subscriberMessages);

                        }
                    }
                }
            }
        }
    }

}
