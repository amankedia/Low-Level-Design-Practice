public class SubscriberImpl extends Subscriber {

    public String name;
    public SubscriberImpl(String name){
        super(name);
    }

    public void addSubscriber(String topic, PubSubService pubSubService){
        pubSubService.addSubscriber(topic, this);
    }
    public void unSubscribe(String topic, PubSubService pubSubService){
        pubSubService.removeSubscribers(topic, this);
    }
    public void getMessagesForSubscriberOfTopic(String topic, PubSubService pubSubService){
        pubSubService.getMessagesForSubscriberOfTopic(topic, this);
    }

}
